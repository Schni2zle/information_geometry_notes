"""Chapter 2 worked examples: computes and asserts every number quoted in the notes.

Run: python3 ch2_examples.py
Conventions follow Amari and Nagaoka (2000): l = log p, g_ij = E[d_i l d_j l] (2.6),
Gamma^(alpha)_{ij,k} = E[(d_i d_j l + (1 - alpha)/2 d_i l d_j l) d_k l] (2.25), T_ijk = E[d_i l d_j l d_k l] (2.28).
"""

from itertools import product
from math import comb

import numpy as np
import sympy as sp
from scipy import integrate, stats
from scipy.special import gamma as Gamma_fn


def close(a, b, tol=5e-4):
    return abs(float(a) - float(b)) < tol


x = sp.symbols("x", real=True)
mu = sp.symbols("mu", real=True)
sig, p, xi, tau, al = sp.symbols("sigma p xi tau alpha", positive=True)


def normal_expect(expr):
    """E[expr] under N(mu, sigma^2), via the moment generating approach in sympy."""
    dens = sp.exp(-((x - mu) ** 2) / (2 * sig**2)) / (sp.sqrt(2 * sp.pi) * sig)
    return sp.simplify(sp.integrate(sp.expand(expr) * dens, (x, -sp.oo, sp.oo)))


# ---------------------------------------------------------------- 2.1 Statistical models
print("2.1 Statistical models")
for k, n_expected in ((3, 9), (10, 65)):
    assert k + k * (k + 1) // 2 == n_expected
xi_pt = (0.2, 0.3)
p_pt = (1 - sum(xi_pt),) + xi_pt
print("  P(X) with 3 points, xi = (0.2, 0.3) -> p =", tuple(round(v, 10) for v in p_pt))
assert np.allclose(p_pt, (0.5, 0.2, 0.3))
# score has mean zero for the normal family (2.4)
l_norm = -((x - mu) ** 2) / (2 * sig**2) - sp.log(sig) - sp.log(2 * sp.pi) / 2
assert normal_expect(sp.diff(l_norm, mu)) == 0 and normal_expect(sp.diff(l_norm, sig)) == 0
# uniform U(0, xi): support depends on xi, the score is -1/xi everywhere, mean -1/xi != 0
score_unif = sp.diff(-sp.log(xi), xi)
assert score_unif == -1 / xi

# ---------------------------------------------------------------- 2.2 Fisher metric
print("2.2 Fisher metric")
dl = [sp.diff(l_norm, v) for v in (mu, sig)]
G = sp.Matrix(2, 2, lambda i, j: normal_expect(dl[i] * dl[j]))
G_hess = sp.Matrix(2, 2, lambda i, j: -normal_expect(sp.diff(l_norm, (mu, sig)[i], (mu, sig)[j])))
print("  normal Fisher matrix (2.6):", G, " (2.8):", G_hess)
assert G == sp.diag(1 / sig**2, 2 / sig**2) and G_hess == G
# (2.10) numerically at (mu, sigma) = (1, 2)
m0, s0 = 1.0, 2.0
f = lambda t, m, s: stats.norm.pdf(t, m, s)
h = 1e-5
dsqrt_mu = lambda t: (np.sqrt(f(t, m0 + h, s0)) - np.sqrt(f(t, m0 - h, s0))) / (2 * h)
dsqrt_sig = lambda t: (np.sqrt(f(t, m0, s0 + h)) - np.sqrt(f(t, m0, s0 - h))) / (2 * h)
g_mm = 4 * integrate.quad(lambda t: dsqrt_mu(t) ** 2, -40, 40)[0]
g_ss = 4 * integrate.quad(lambda t: dsqrt_sig(t) ** 2, -40, 40)[0]
print("  (2.10) at (1, 2): g_mumu =", round(g_mm, 6), " g_sigsig =", round(g_ss, 6))
assert close(g_mm, 0.25, 1e-6) and close(g_ss, 0.5, 1e-6)
# Poisson and Bernoulli
assert sp.simplify(sp.summation(0, (x, 0, 1))) == 0
g_bern = sp.simplify(p * (1 / p) ** 2 + (1 - p) * (1 / (1 - p)) ** 2)
assert sp.simplify(g_bern - 1 / (p * (1 - p))) == 0
print("  Bernoulli g at p = 0.3:", float(g_bern.subs(p, 0.3)))
assert close(g_bern.subs(p, sp.Rational(3, 10)), 4.7619)
# sign of a N(mu, 1) observation: information mu-> phi^2 / (Phi (1 - Phi))
GY0 = stats.norm.pdf(0) ** 2 / (0.5 * 0.5)
print("  info in sign(X) at mu = 0:", round(GY0, 4), " loss:", round(1 - GY0, 4))
assert close(GY0, 2 / np.pi, 1e-12) and close(GY0, 0.6366) and close(1 - GY0, 0.3634)
GY1 = stats.norm.pdf(1) ** 2 / (stats.norm.cdf(1) * stats.norm.sf(1))
print("  info in sign(X) at mu = 1:", round(GY1, 4))
assert close(GY1, 0.4386)
# Delta G formula (2.18) at mu = 0: E[Var(score | Y)], score = X - mu, given sign
var_half = 1 - 2 / np.pi  # variance of a half-normal
assert close(var_half, 1 - GY0, 1e-12)


# convexity (2.23): 0.5 N(xi, 1) + 0.5 N(xi, 4) at xi = 0
def mix_info(lam, s1=1.0, s2=2.0):
    def integrand(t):
        pdf = lam * stats.norm.pdf(t, 0, s1) + (1 - lam) * stats.norm.pdf(t, 0, s2)
        dpdf = lam * stats.norm.pdf(t, 0, s1) * t / s1**2 + (1 - lam) * stats.norm.pdf(t, 0, s2) * t / s2**2
        return dpdf**2 / pdf

    return integrate.quad(integrand, -60, 60)[0]


Gmix = mix_info(0.5)
print("  mixture 0.5 N(xi,1) + 0.5 N(xi,4): G =", round(Gmix, 4), "<= 0.625")
assert Gmix < 0.625 and close(Gmix, 0.4615)
# Cramer-Rao: sample variance with N = 10, v = 1
N = 10
assert close(2 / N, 0.2, 1e-12) and close(2 / (N - 1), 0.2222)

# ---------------------------------------------------------------- 2.3 alpha-connection
print("2.3 alpha-connection")
coords = (mu, sig)
T = {}
for i in range(2):
    for j in range(2):
        for k in range(2):
            T[(i, j, k)] = normal_expect(dl[i] * dl[j] * dl[k])
print("  normal T: T_mumusig =", T[(0, 0, 1)], " T_sigsigsig =", T[(1, 1, 1)], " T_mumumu =", T[(0, 0, 0)], " T_musigsig =", T[(0, 1, 1)])
assert T[(0, 0, 1)] == 2 / sig**3 and T[(1, 1, 1)] == 8 / sig**3 and T[(0, 0, 0)] == 0 and T[(0, 1, 1)] == 0


def gamma_alpha(i, j, k, a):
    return sp.simplify(normal_expect((sp.diff(l_norm, coords[i], coords[j]) + (1 - sp.S(a)) / 2 * dl[i] * dl[j]) * dl[k]))


G0 = {(i, j, k): gamma_alpha(i, j, k, 0) for i in range(2) for j in range(2) for k in range(2)}
# Levi-Civita from (1.69)
LC = {(i, j, k): sp.simplify(sp.Rational(1, 2) * (sp.diff(G[j, k], coords[i]) + sp.diff(G[k, i], coords[j]) - sp.diff(G[i, j], coords[k]))) for i in range(2) for j in range(2) for k in range(2)}
assert G0 == LC
print("  Gamma^(0): mumu,sig =", G0[(0, 0, 1)], " musig,mu =", G0[(0, 1, 0)], " sigsig,sig =", G0[(1, 1, 1)])
for key in G0:
    ga = gamma_alpha(*key, al)
    assert sp.simplify(ga - (G0[key] - al / 2 * T[key])) == 0  # (2.27) with beta = 0
assert sp.simplify(gamma_alpha(0, 0, 1, 1)) == 0  # 1/sigma^3 - (1/2)(2/sigma^3)
# metricity check (2.30): d_k g_ij = Gamma^(0)_{ki,j} + Gamma^(0)_{kj,i}; fails for alpha = 1
lhs = sp.diff(G[0, 0], sig)
assert sp.simplify(lhs - (G0[(1, 0, 0)] + G0[(1, 0, 0)])) == 0
G1 = {key: gamma_alpha(*key, 1) for key in G0}
Gm1 = {key: gamma_alpha(*key, -1) for key in G0}
print("  Gamma^(1):", G1)
print("  Gamma^(-1):", Gm1)
assert sp.simplify(lhs - (G1[(1, 0, 0)] + G1[(1, 0, 0)])) != 0
assert sp.simplify(lhs - (G1[(1, 0, 0)] + Gm1[(1, 0, 0)])) == 0  # duality preview (3.2)
# exponential-family form of the normal: psi in natural parameters
t1, t2 = sp.symbols("theta1 theta2", real=True)
psi = -(t1**2) / (4 * t2) + sp.log(-sp.pi / t2) / 2
psi_val = psi.subs({t1: sp.Rational(1, 4), t2: sp.Rational(-1, 8)})
psi_direct = sp.Rational(1, 8) + sp.log(sp.sqrt(2 * sp.pi) * 2)
print("  psi at theta = (0.25, -0.125):", float(psi_val))
assert sp.simplify(psi_val - psi_direct) == 0 and close(psi_val, 1.7371)
# Fisher metric = Hessian of psi; transform back to (mu, sigma)
H = sp.hessian(psi, (t1, t2))
th_of = {t1: mu / sig**2, t2: -1 / (2 * sig**2)}
J = sp.Matrix([mu / sig**2, -1 / (2 * sig**2)]).jacobian([mu, sig])
assert sp.simplify(J.T * H.subs(th_of) * J - G) == sp.zeros(2, 2)
# Bernoulli in the mean parameter p: T, Gamma^(alpha) = -(1 + alpha)/2 T, so Gamma^(-1) = 0
dlb = {0: -1 / (1 - p), 1: 1 / p}
d2lb = {0: -1 / (1 - p) ** 2, 1: -1 / p**2}
probs = {0: 1 - p, 1: p}
Tb = sp.simplify(sum(probs[v] * dlb[v] ** 3 for v in (0, 1)))
assert sp.simplify(Tb - (1 - 2 * p) / (p**2 * (1 - p) ** 2)) == 0
print("  Bernoulli T at p = 0.3:", float(Tb.subs(p, sp.Rational(3, 10))))
assert close(Tb.subs(p, sp.Rational(3, 10)), 9.0703)
Gab = sp.simplify(sum(probs[v] * (d2lb[v] + (1 - al) / 2 * dlb[v] ** 2) * dlb[v] for v in (0, 1)))
assert sp.simplify(Gab + (1 + al) / 2 * Tb) == 0
# Bernoulli in natural parameter theta: Gamma^(1) = 0
th = sp.symbols("theta", real=True)
pth = sp.exp(th) / (1 + sp.exp(th))
dl_th = {0: -pth, 1: 1 - pth}  # d/dtheta [x theta - log(1 + e^theta)]
d2_th = -pth * (1 - pth)
G1_th = sp.simplify(sum({0: 1 - pth, 1: pth}[v] * d2_th * dl_th[v] for v in (0, 1)))
assert G1_th == 0
# N(mu, 1) is an affine line theta2 = -1/2; N(mu, mu^2) is the parabola theta2 = -theta1^2/2

# ---------------------------------------------------------------- 2.4 Chentsov
print("2.4 Chentsov")
r = {0: 0.3, 2: 0.7, 1: 0.6, 3: 0.4}  # p(x | F(x)) with F(x) = x mod 2
for pv in (0.3,):
    pS = {xx: (1 - pv if xx % 2 == 0 else pv) * r[xx] for xx in range(4)}
    dS = {xx: (-1 / (1 - pv) if xx % 2 == 0 else 1 / pv) for xx in range(4)}
    gS = sum(pS[xx] * dS[xx] ** 2 for xx in range(4))
    TS = sum(pS[xx] * dS[xx] ** 3 for xx in range(4))
    print("  4-point model: g =", round(gS, 4), " T =", round(TS, 4))
    assert close(gS, 4.7619) and close(TS, 9.0703)
# Euclidean metric is not invariant: sum (dp/dp)^2 on 2 points = 2, on 4 points = 1.1
e2 = 1 + 1
e4 = sum(r[xx] ** 2 for xx in range(4))
print("  Euclidean 'metric': 2 points", e2, " 4 points", round(e4, 4))
assert e2 == 2 and close(e4, 1.1, 1e-12)

# n Bernoulli(xi) trials: F = number of successes (sufficient) vs F = first trial only
n_tr, xv = 10, 0.3
wv = xv * (1 - xv)


def trials_structure(pairs):
    """g, T and Gamma^(alpha) for alpha = 1, 0, -1 from (probability, number of successes) pairs."""
    g_, T_, E21 = 0.0, 0.0, 0.0
    for pr, s in pairs:
        d1 = s / xv - (n_tr - s) / (1 - xv)
        d2 = -s / xv**2 - (n_tr - s) / (1 - xv) ** 2
        g_ += pr * d1**2
        T_ += pr * d1**3
        E21 += pr * d2 * d1
    return g_, T_, [E21 + (1 - a) / 2 * T_ for a in (1, 0, -1)]


seqs = [(xv ** sum(bits) * (1 - xv) ** (n_tr - sum(bits)), sum(bits)) for bits in product((0, 1), repeat=n_tr)]
counts = [(comb(n_tr, y) * xv**y * (1 - xv) ** (n_tr - y), y) for y in range(n_tr + 1)]
on_S, on_SF = trials_structure(seqs), trials_structure(counts)
print("  10 trials, xi = 0.3: sequences g, T =", round(on_S[0], 4), round(on_S[1], 4), " counts g, T =", round(on_SF[0], 4), round(on_SF[1], 4))
for gT in (on_S, on_SF):
    assert close(gT[0], 47.619) and close(gT[1], 90.703)
    assert all(close(a, b) for a, b in zip(gT[2], (-90.703, -45.3515, 0.0)))
assert close(n_tr / wv, 47.619) and close(n_tr * (1 - 2 * xv) / wv**2, 90.703)
g_first = 1 / wv  # F = first trial: Bernoulli(xi)
loss = on_S[0] - g_first
print("  first trial only: g' =", round(g_first, 4), " loss =", round(loss, 4))
assert close(g_first, 4.762) and close(loss, 42.857) and close(loss, (n_tr - 1) / wv)

# ---------------------------------------------------------------- 2.5 Geometry of P(X)
print("2.5 Geometry of P(X)")
P = np.array([0.5, 0.3, 0.2])
Q = np.array([0.2, 0.3, 0.5])
Xm = np.array([0.1, -0.1, 0.0])
Xe = Xm / P
print("  X^(e) =", Xe.round(4), " |X|^2 =", round(float(Xm @ Xe), 5))
assert np.allclose(Xe, [0.2, -0.3333, 0.0], atol=1e-4) and close(Xm @ Xe, 0.05333, 1e-5)
c = Q @ Xe
Xe_q = Xe - c
Xm_q = Q * Xe_q
print("  E_q[X^(e)] =", round(c, 4), " e-transported X^(e) =", Xe_q.round(5), " X^(m) =", Xm_q.round(4))
assert close(c, -0.06, 1e-12) and np.allclose(Xe_q, [0.26, -0.27333, 0.06], atol=1e-5)
assert np.allclose(Xm_q, [0.052, -0.082, 0.03], atol=1e-4) and close(Xm_q.sum(), 0, 1e-12)
norm_e_q = Q @ Xe_q**2
print("  |Pi^e X|^2 at q =", round(norm_e_q, 5), " <Pi^e X, Pi^m X>_q =", round(Xe_q @ Xm, 5))
assert close(norm_e_q, 0.03773, 1e-5) and close(Xe_q @ Xm, 0.05333, 1e-5)
norm_m_q = Xm @ (Xm / Q)
print("  |Pi^m X|^2 at q =", round(norm_m_q, 5))
assert close(norm_m_q, 0.08333, 1e-5)
# Theorem 2.7: A = (1, 2, 4) at p = (0.5, 0.3, 0.2)
A = np.array([1.0, 2.0, 4.0])
EA = P @ A
VA = P @ (A - EA) ** 2
xi2 = P[1:]
Ginv = np.diag(xi2) - np.outer(xi2, xi2)
dE = A[1:] - A[0]
print("  E[A] =", EA, " V[A] =", round(VA, 4), " |dE|^2 =", round(dE @ Ginv @ dE, 4))
assert close(EA, 1.9, 1e-12) and close(VA, 1.29, 1e-12) and close(dE @ Ginv @ dE, 1.29, 1e-12)
assert np.allclose(Ginv, [[0.21, -0.06], [-0.06, 0.16]])
# Jeffreys normalisers V = pi^((n+1)/2) / Gamma((n+1)/2)
V1 = integrate.quad(lambda s: 1 / np.sqrt(s * (1 - s)), 0, 1)[0]
V2 = integrate.dblquad(lambda b, a: 1 / np.sqrt(a * b * (1 - a - b)), 0, 1, 0, lambda a: 1 - a)[0]
print("  Jeffreys V for n = 1:", round(V1, 4), " n = 2:", round(V2, 4))
assert close(V1, np.pi) and close(np.pi ** 1 / Gamma_fn(1), np.pi, 1e-12)
assert close(V2, 2 * np.pi, 1e-3) and close(np.pi**1.5 / Gamma_fn(1.5), 2 * np.pi, 1e-12)
# sphere of radius 2 and the Fisher-Rao distance
assert close(np.sum((2 * np.sqrt(P)) ** 2), 4.0, 1e-12)
BC = np.sum(np.sqrt(P * Q))
d_FR = 2 * np.arccos(BC)
print("  Bhattacharyya coefficient =", round(BC, 5), " Fisher-Rao distance =", round(d_FR, 4))
assert close(BC, 0.93246, 1e-5) and close(d_FR, 0.7393)
# Bernoulli check of the distance formula against the integral of sqrt(g)
pa, pb = 0.3, 0.6
d_int = integrate.quad(lambda s: 1 / np.sqrt(s * (1 - s)), pa, pb)[0]
d_cl = 2 * np.arccos(np.sqrt(pa * pb) + np.sqrt((1 - pa) * (1 - pb)))
print("  Bernoulli 0.3 -> 0.6: integral", round(d_int, 4), " closed form", round(d_cl, 4))
assert close(d_int, d_cl, 1e-8) and close(d_int, 0.6129)

# ---------------------------------------------------------------- 2.6 alpha-families
print("2.6 alpha-families")
# alpha-representations of X at p and the pairing (2.60)
for a_val, expected in ((1, [0.2, -0.3333, 0.0]), (0, [0.1414, -0.1826, 0.0]), (-1, [0.1, -0.1, 0.0])):
    Xa = P ** ((1 - a_val) / 2) * Xe
    assert np.allclose(Xa, expected, atol=1e-4)
for a_val in (0.5, 2.0, -3.0):
    Xa = P ** ((1 - a_val) / 2) * Xe
    Xma = P ** ((1 + a_val) / 2) * Xe
    assert close(Xa @ Xma, 0.05333, 1e-5)
# denormalisation of Bernoulli: check (2.67)-(2.70) from (2.60)-(2.61)
pt_vals = {0: tau * (1 - xi), 1: tau * xi}


def Lalpha(u, a):
    return sp.Piecewise((sp.log(u), sp.Eq(a, 1)), (2 / (1 - a) * u ** ((1 - a) / 2), True))


def ell(v, a):
    return 2 / (1 - a) * pt_vals[v] ** ((1 - a) / 2)


crd = (xi, tau)
a_num = sp.Rational(1, 3)  # a generic alpha
gt = sp.Matrix(2, 2, lambda i, j: sp.simplify(sum(sp.diff(ell(v, a_num), crd[i]) * sp.diff(ell(v, -a_num), crd[j]) for v in (0, 1))))
gS = 1 / (xi * (1 - xi))
assert sp.simplify(gt - sp.diag(tau * gS, 1 / tau)) == sp.zeros(2, 2)


def Gt(i, j, k, a):
    return sp.simplify(sum(sp.diff(ell(v, a), crd[i], crd[j]) * sp.diff(ell(v, -a), crd[k]) for v in (0, 1)))


assert sp.simplify(Gt(1, 1, 1, a_num) + (1 + a_num) / 2 / tau**2) == 0  # (2.70)
assert sp.simplify(Gt(1, 1, 0, a_num)) == 0
assert sp.simplify(Gt(0, 0, 1, a_num) + (1 + a_num) / 2 * gS) == 0  # (2.68)
assert sp.simplify(Gt(0, 1, 0, a_num) - (1 - a_num) / 2 * gS) == 0  # (2.69)
# interpolating p0 = (0.5, 0.3, 0.2) and p1 = (0.2, 0.3, 0.5) at t = 1/2
p0, p1 = P, Q
m_mid = 0.5 * p0 + 0.5 * p1
e_mid = np.sqrt(p0 * p1) / np.sum(np.sqrt(p0 * p1))
z_mid = (0.5 * np.sqrt(p0) + 0.5 * np.sqrt(p1)) ** 2
z_mid = z_mid / z_mid.sum()
print("  midpoints: m", m_mid.round(4), " e", e_mid.round(4), " 0", z_mid.round(4))
assert np.allclose(m_mid, [0.35, 0.3, 0.35]) and np.allclose(e_mid, [0.3391, 0.3217, 0.3391], atol=1e-4)
assert np.allclose(z_mid, [0.3448, 0.3105, 0.3448], atol=1e-4)
# the 0-curve lies on the great circle: distance p0 -> mid = mid -> p1 = half of d_FR
d1 = 2 * np.arccos(np.sum(np.sqrt(p0 * z_mid)))
assert close(d1, d_FR / 2, 1e-9)
print("All chapter 2 numbers verified.")
