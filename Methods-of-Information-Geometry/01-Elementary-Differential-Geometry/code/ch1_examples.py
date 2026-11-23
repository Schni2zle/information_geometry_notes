"""Chapter 1 worked examples: computes and asserts every number quoted in the notes.

Run: python3 ch1_examples.py
Index conventions follow Amari and Nagaoka (2000):
  nabla_{d_i} d_j = Gamma^k_{ij} d_k                      (1.39)
  R(d_i, d_j) d_k = R^l_{ijk} d_l                           (1.44)
  R^l_{ijk} = d_i G^l_{jk} - d_j G^l_{ik} + G^h_{jk} G^l_{ih} - G^h_{ik} G^l_{jh}   (1.45)
  T^k_{ij} = G^k_{ij} - G^k_{ji}                           (1.46)
"""

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


def close(a, b, tol=5e-4):
    return abs(float(a) - float(b)) < tol


def christoffel_second_kind(g, coords):
    """Gamma^k_{ij} of the Levi-Civita connection, from (1.69) raised with g^{-1}."""
    n = len(coords)
    ginv = sp.simplify(g.inv())
    first = [[[sp.Rational(1, 2) * (sp.diff(g[j, k], coords[i]) + sp.diff(g[k, i], coords[j]) - sp.diff(g[i, j], coords[k])) for k in range(n)] for j in range(n)] for i in range(n)]
    return [[[sp.simplify(sum(first[i][j][m] * ginv[m, k] for m in range(n))) for j in range(n)] for i in range(n)] for k in range(n)]
    # indexed as G[k][i][j] = Gamma^k_{ij}


def riemann(G, coords):
    """R^l_{ijk} from (1.45); G[k][i][j] = Gamma^k_{ij}."""
    n = len(coords)
    R = {}
    for l in range(n):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    val = sp.diff(G[l][j][k], coords[i]) - sp.diff(G[l][i][k], coords[j])
                    val += sum(G[h][j][k] * G[l][i][h] - G[h][i][k] * G[l][j][h] for h in range(n))
                    R[(l, i, j, k)] = sp.simplify(val)
    return R


def gaussian_curvature(g, R):
    """K = <R(d1, d2) d2, d1> / det g for a 2-dimensional manifold."""
    num = sum(g[l, 0] * R[(l, 0, 1, 1)] for l in range(2))
    return sp.simplify(num / g.det())


r, th, ph, mu, sig, v, t = sp.symbols("r theta phi mu sigma v t", positive=True)
x, y = sp.symbols("x y", real=True)

# ---------------------------------------------------------------- 1.1 Differentiable manifolds
print("1.1 Differentiable manifolds")
J_xy_rth = sp.Matrix([[sp.cos(th), -r * sp.sin(th)], [sp.sin(th), r * sp.cos(th)]])  # d(x,y)/d(r,theta)
at = {r: 2, th: sp.pi / 3}
J1 = np.array(J_xy_rth.subs(at).evalf(), dtype=float)
J2 = np.linalg.inv(J1)
print("  d(x,y)/d(r,theta) at (2, pi/3) =\n", J1.round(4))
print("  d(r,theta)/d(x,y) =\n", J2.round(4))
assert np.allclose(J1, [[0.5, -1.7321], [0.8660, 1.0]], atol=1e-4)
assert np.allclose(J2, [[0.5, 0.8660], [-0.4330, 0.25]], atol=1e-4)
assert close(np.linalg.det(J1), 2.0)
assert np.allclose(J1 @ J2, np.eye(2))

# normal family: (mu, sigma) -> natural parameters (theta1, theta2) = (mu/sigma^2, -1/(2 sigma^2))
nat = sp.Matrix([mu / sig**2, -1 / (2 * sig**2)])
Jn = nat.jacobian([mu, sig])
pt = {mu: 1, sig: 2}
print("  theta at (mu, sigma) = (1, 2):", [float(e) for e in nat.subs(pt)])
print("  d(theta)/d(mu, sigma) =", np.array(Jn.subs(pt), dtype=float).tolist(), "det", float(Jn.det().subs(pt)))
assert [float(e) for e in nat.subs(pt)] == [0.25, -0.125]
assert np.allclose(np.array(Jn.subs(pt), dtype=float), [[0.25, -0.25], [0, 0.125]])
assert sp.simplify(Jn.det() - 1 / sig**5) == 0 and float(Jn.det().subs(pt)) == 0.03125

# ---------------------------------------------------------------- 1.2 Tangent vectors
print("1.2 Tangent vectors")
# curve gamma(t) = (t, t^2) at t = 1, p = (1, 1)
gx, gy = t, t**2
rt, tht = sp.sqrt(gx**2 + gy**2), sp.atan2(gy, gx)
rdot = sp.diff(rt, t).subs(t, 1)
thdot = sp.diff(tht, t).subs(t, 1)
print("  polar components (r', theta') =", float(rdot), float(thdot))
assert sp.simplify(rdot - 3 / sp.sqrt(2)) == 0 and close(rdot, 2.1213)
assert sp.simplify(thdot - sp.Rational(1, 2)) == 0
# derivative of f = x^2 + y^2 = r^2 along the curve, in both coordinate systems
df_cart = (2 * gx * sp.diff(gx, t) + 2 * gy * sp.diff(gy, t)).subs(t, 1)
df_polar = 2 * rt.subs(t, 1) * rdot
assert df_cart == 6 and sp.simplify(df_polar - 6) == 0
# differential of (mu, sigma) -> theta applied to d_sigma at (1, 2)
dl = Jn.subs(pt) * sp.Matrix([0, 1])
print("  d(lambda)(d_sigma) =", [float(e) for e in dl])
assert [float(e) for e in dl] == [-0.25, 0.125]

# ---------------------------------------------------------------- 1.3 Vector fields and tensor fields
print("1.3 Vector and tensor fields")
# d_x in polar coordinates: components d(r,theta)/dx
dx_polar = sp.Matrix([sp.cos(th), -sp.sin(th) / r])
comp = [float(e) for e in dx_polar.subs(at)]
print("  d_x = cos(theta) d_r - sin(theta)/r d_theta at (2, pi/3):", comp)
assert np.allclose(comp, [0.5, -0.4330], atol=1e-4)
# Euclidean metric transforms to diag(1, r^2) by (1.22)
g_polar = sp.simplify(J_xy_rth.T * J_xy_rth)
assert g_polar == sp.diag(1, r**2)
# Lie bracket is not F-linear: [d_x, x d_y] = d_y while x [d_x, d_y] = 0
f = sp.Function("f")(x, y)
bracket = sp.diff(x * sp.diff(f, y), x) - x * sp.diff(sp.diff(f, x), y)
assert sp.simplify(bracket - sp.diff(f, y)) == 0

# ---------------------------------------------------------------- 1.4 Submanifolds
print("1.4 Submanifolds")
X3 = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
B = X3.jacobian([th, ph])
sat = {th: sp.pi / 3, ph: sp.pi / 4}
Bn = np.array(B.subs(sat).evalf(), dtype=float)
print("  B_theta =", Bn[:, 0].round(4), " B_phi =", Bn[:, 1].round(4))
assert np.allclose(Bn[:, 0], [0.3536, 0.3536, -0.8660], atol=1e-4)
assert np.allclose(Bn[:, 1], [-0.6124, 0.6124, 0.0], atol=1e-4)
assert np.linalg.matrix_rank(Bn) == 2
g_sphere = sp.simplify(B.T * B)
assert g_sphere == sp.diag(1, sp.sin(th) ** 2)
# cusp (t^2, t^3) has zero velocity at t = 0: condition (ii) fails
assert sp.Matrix([2 * t, 3 * t**2]).subs(t, 0) == sp.Matrix([0, 0])
# N(mu, mu^2) in natural parameters: theta2 = -theta1^2 / 2
c = sp.Matrix([1 / mu, -1 / (2 * mu**2)])
assert sp.simplify(c[1] + c[0] ** 2 / 2) == 0

# ---------------------------------------------------------------- 1.5 Riemannian metrics
print("1.5 Riemannian metrics")
g_fisher = sp.diag(1 / sig**2, 2 / sig**2)  # Fisher metric of N(mu, sigma^2), derived in 2.2
L_vert = sp.integrate(sp.sqrt(2) / sig, (sig, 1, 2))
print("  length of sigma: 1 -> 2 at fixed mu =", float(L_vert))
assert sp.simplify(L_vert - sp.sqrt(2) * sp.log(2)) == 0 and close(L_vert, 0.9803)
assert sp.integrate(1 / sp.Integer(1), (mu, 0, 1)) == 1
assert sp.integrate(sp.Rational(1, 2), (mu, 0, 1)) == sp.Rational(1, 2)
# change to (mu, v = sigma^2) with (1.22)
Jv = sp.diag(1, sp.diff(sp.sqrt(v), v))  # d(mu, sigma)/d(mu, v)
g_v = sp.simplify(Jv.T * g_fisher.subs(sig, sp.sqrt(v)) * Jv)
print("  metric in (mu, v):", g_v, "at v = 4:", g_v.subs(v, 4))
assert g_v == sp.diag(1 / v, 1 / (2 * v**2))
assert g_v.subs(v, 4) == sp.diag(sp.Rational(1, 4), sp.Rational(1, 32))
# latitude theta = pi/3 on the unit sphere
L_lat = 2 * sp.pi * sp.sin(sp.pi / 3)
print("  latitude pi/3 length =", float(L_lat))
assert close(L_lat, 5.4414)

# ---------------------------------------------------------------- 1.6 Affine connections
print("1.6 Affine connections")
# (1.29) with Gamma = 0 in Cartesian: tilde Gamma^t_{rs} = d^2 xi^k / drho^r drho^s * drho^t / dxi^k
xi = sp.Matrix([r * sp.cos(th), r * sp.sin(th)])
rho = [r, th]
Jinv = sp.simplify(J_xy_rth.inv())  # d(r,theta)/d(x,y)
Gpolar = [[[sp.simplify(sum(sp.diff(xi[k], rho[a], rho[b]) * Jinv[tt, k] for k in range(2))) for b in range(2)] for a in range(2)] for tt in range(2)]
print("  polar Gamma: G^r_thth =", Gpolar[0][1][1], " G^th_rth =", Gpolar[1][0][1], " G^th_thr =", Gpolar[1][1][0])
assert Gpolar[0][1][1] == -r and Gpolar[1][0][1] == 1 / r and Gpolar[1][1][0] == 1 / r
assert Gpolar[0][0][0] == 0 and Gpolar[0][0][1] == 0 and Gpolar[1][0][0] == 0 and Gpolar[1][1][1] == 0
# Levi-Civita of diag(1, r^2) gives the same symbols
assert christoffel_second_kind(sp.diag(1, r**2), [r, th]) == Gpolar


# parallel transport along the circle r = 2, theta = t, from X = d_r
def circle_rhs(s, X, R0=2.0):
    Xr, Xth = X
    return [R0 * Xth, -Xr / R0]  # X^k' + gamma'^i X^j Gamma^k_ij = 0 with gamma' = (0, 1)


sol = solve_ivp(circle_rhs, [0, np.pi / 2], [1.0, 0.0], rtol=1e-11, atol=1e-12)
Xr_end, Xth_end = sol.y[:, -1]
print("  transported d_r after a quarter turn: X^r =", round(Xr_end, 6), " X^theta =", round(Xth_end, 6))
assert close(Xr_end, 0.0, 1e-6) and close(Xth_end, -0.5, 1e-6)
# Cartesian picture: X = X^r e_r + X^theta d_theta, with d_theta = (-r sin, r cos)
e_r = np.array([0.0, 1.0])
d_th = np.array([-2.0, 0.0])
assert np.allclose(Xr_end * e_r + Xth_end * d_th, [1.0, 0.0], atol=1e-6)

# ---------------------------------------------------------------- 1.7 Flatness
print("1.7 Flatness")
Rpolar = riemann(Gpolar, [r, th])
assert all(val == 0 for val in Rpolar.values())
# a connection on R^2 with torsion: only Gamma^1_{12} = 1 in Cartesian coordinates
Gt = [[[0, 1], [0, 0]], [[0, 0], [0, 0]]]
Rt = riemann([[[sp.Integer(e) for e in row] for row in mat] for mat in Gt], [x, y])
T112 = Gt[0][0][1] - Gt[0][1][0]
print("  torsion T^1_12 =", T112, " curvature all zero:", all(val == 0 for val in Rt.values()))
assert T112 == 1 and all(val == 0 for val in Rt.values())
# its parallel fields (1.40): d_1 and -x d_1 + d_2; their bracket is -d_1, so no affine coordinates exist
for Xf in (sp.Matrix([1, 0]), sp.Matrix([-x, 1])):
    for i, xi_ in enumerate((x, y)):
        for k in range(2):
            assert sp.diff(Xf[k], xi_) + sum(Xf[j] * Gt[k][i][j] for j in range(2)) == 0
P1, P2 = sp.Matrix([1, 0]), sp.Matrix([-x, 1])
bracket_P = P2.jacobian([x, y]) * P1 - P1.jacobian([x, y]) * P2
assert bracket_P == sp.Matrix([-1, 0])
# sphere: curvature of the Levi-Civita connection
Gs = christoffel_second_kind(sp.diag(1, sp.sin(th) ** 2), [th, ph])
Rs = riemann(Gs, [th, ph])
K_sphere = gaussian_curvature(sp.diag(1, sp.sin(th) ** 2), Rs)
print("  unit sphere: R^th_{ph th ph} =", Rs[(0, 1, 0, 1)], " K =", K_sphere)
assert K_sphere == 1
assert sp.simplify(Rs[(0, 1, 0, 1)] + sp.sin(th) ** 2) == 0
# affine map (x, y) -> (2x + y + 1, x - y): regular A
A = np.array([[2, 1], [1, -1]])
assert close(np.linalg.det(A), -3.0, 1e-12)

# ---------------------------------------------------------------- 1.8 Autoparallel submanifolds
print("1.8 Autoparallel submanifolds")
# line x = 1 parametrised by (1, t): polar geodesic equations hold
rl, thl = sp.sqrt(1 + t**2), sp.atan(t)
eq_r = sp.simplify(sp.diff(rl, t, 2) + Gpolar[0][1][1] .subs(r, rl) * sp.diff(thl, t) ** 2)
eq_th = sp.simplify(sp.diff(thl, t, 2) + 2 * Gpolar[1][0][1].subs(r, rl) * sp.diff(rl, t) * sp.diff(thl, t))
assert eq_r == 0 and eq_th == 0
# non-affine parameter (1, t^3): acceleration = (2/t) velocity
vel = sp.Matrix([0, 3 * t**2])
acc = sp.diff(vel, t)
assert sp.simplify(acc - (2 / t) * vel) == sp.zeros(2, 1)
# great circle on the unit sphere (equator theta = pi/2) solves the sphere geodesic equations
eq1 = sp.simplify(sp.diff(sp.pi / 2 + 0 * t, t, 2) + Gs[0][1][1].subs(th, sp.pi / 2) * 1)
assert eq1 == 0

# ---------------------------------------------------------------- 1.9 Embedding curvature
print("1.9 Embedding curvature")
a = sp.symbols("a", positive=True)
Xa = a * X3
Ba = Xa.jacobian([th, ph])
n_out = X3  # unit outward normal
H_thth = sp.simplify((sp.diff(Xa, th, 2)).dot(n_out))
H_phph = sp.simplify((sp.diff(Xa, ph, 2)).dot(n_out))
H_thph = sp.simplify((sp.diff(Xa, th, ph)).dot(n_out))
vals = [float(e.subs({a: 2, th: sp.pi / 3})) for e in (H_thth, H_phph, H_thph)]
print("  sphere radius 2 at theta = pi/3: H_thth, H_phph, H_thph =", vals)
assert vals == [-2.0, -1.5, 0.0]
ga = sp.simplify(Ba.T * Ba)
assert sp.simplify(H_thth / ga[0, 0] + 1 / a) == 0 and sp.simplify(H_phph / ga[1, 1] + 1 / a) == 0
# projected connection = Levi-Civita of induced metric: Gamma_{ph ph, th} via (1.62) and (1.69)
proj = sp.simplify(sp.diff(Xa, ph, 2).dot(Ba[:, 0]))
lc = sp.simplify(sp.Rational(1, 2) * (2 * sp.diff(ga[1, 0], ph) - sp.diff(ga[1, 1], th)))
print("  Gamma^(pi)_{ph ph, th} =", proj)
assert sp.simplify(proj - lc) == 0 and sp.simplify(proj + a**2 * sp.sin(th) * sp.cos(th)) == 0
# cylinder radius a: induced metric diag(a^2, 1) is flat, H_uu = -a
u, w = sp.symbols("u w", real=True)
Xc = sp.Matrix([a * sp.cos(u), a * sp.sin(u), w])
nc = sp.Matrix([sp.cos(u), sp.sin(u), 0])
gc = sp.simplify(Xc.jacobian([u, w]).T * Xc.jacobian([u, w]))
assert gc == sp.diag(a**2, 1)
assert sp.simplify(sp.diff(Xc, u, 2).dot(nc) + a) == 0 and sp.diff(Xc, w, 2).dot(nc) == 0

# ---------------------------------------------------------------- 1.10 Riemannian connection
print("1.10 Riemannian connection")
print("  sphere: G^th_phph =", Gs[0][1][1], " G^ph_thph =", Gs[1][0][1])
assert sp.simplify(Gs[0][1][1] + sp.sin(th) * sp.cos(th)) == 0
assert sp.simplify(Gs[1][0][1] - sp.cos(th) / sp.sin(th)) == 0
# holonomy around the latitude theta0 = pi/3 starting from d_theta
th0 = np.pi / 3


def lat_rhs(s, X):
    Xt, Xp = X
    # gamma' = (0, 1); X^k' + X^j Gamma^k_{ph j} = 0
    return [np.sin(th0) * np.cos(th0) * Xp, -np.cos(th0) / np.sin(th0) * Xt]


sol = solve_ivp(lat_rhs, [0, 2 * np.pi], [1.0, 0.0], rtol=1e-11, atol=1e-12)
Xt_end, Xp_end = sol.y[:, -1]
norm_end = Xt_end**2 + np.sin(th0) ** 2 * Xp_end**2
print("  transported d_theta around theta0 = pi/3:", round(Xt_end, 6), round(Xp_end, 6), " |X|^2 =", round(norm_end, 6))
assert close(Xt_end, -1.0, 1e-6) and close(Xp_end, 0.0, 1e-6) and close(norm_end, 1.0, 1e-6)
assert close(2 * np.pi * (1 - np.cos(th0)), np.pi, 1e-12)
# Fisher metric of the normal family: Christoffel symbols, curvature, a geodesic distance
Gf = christoffel_second_kind(g_fisher, [mu, sig])
print("  normal family: G^mu_{mu sig} =", Gf[0][0][1], " G^sig_{mu mu} =", Gf[1][0][0], " G^sig_{sig sig} =", Gf[1][1][1])
assert Gf[0][0][1] == -1 / sig and Gf[1][0][0] == 1 / (2 * sig) and Gf[1][1][1] == -1 / sig
assert Gf[0][0][0] == 0 and Gf[0][1][1] == 0 and Gf[1][0][1] == 0
K_fisher = gaussian_curvature(g_fisher, riemann(Gf, [mu, sig]))
print("  Gaussian curvature of the normal family =", K_fisher)
assert K_fisher == sp.Rational(-1, 2)
# the vertical line mu = 0 is a geodesic: sigma(s) = exp(s / sqrt 2) has unit speed
s = sp.symbols("s", real=True)
sg = sp.exp(s / sp.sqrt(2))
assert sp.simplify(sp.diff(sg, s, 2) + Gf[1][1][1].subs(sig, sg) * sp.diff(sg, s) ** 2) == 0
assert sp.simplify(2 / sg**2 * sp.diff(sg, s) ** 2 - 1) == 0
print("All chapter 1 numbers verified.")
