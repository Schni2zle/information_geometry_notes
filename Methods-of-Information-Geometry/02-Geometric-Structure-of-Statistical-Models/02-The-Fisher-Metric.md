---
type: concept
tier: core
status: solid
section: 2.2
pages: 28-32
prereqs: [statistical-models, riemannian-metrics]
est_hours: 4
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 2.2, Rao - Information and the Accuracy Attainable in the Estimation of Statistical Parameters (Bull Calcutta Math Soc 1945), Lehmann and Casella - Theory of Point Estimation 2nd ed ch 2 and 6, Cover and Thomas - Elements of Information Theory 2nd ed ch 11]
---

# The Fisher Metric

## TL;DR

- The Fisher information matrix is $g_{ij}(\xi) = E_\xi[\partial_i\ell_\xi\,\partial_j\ell_\xi]$ with $\ell_\xi = \log p(x; \xi)$ (2.6); equivalently $-E_\xi[\partial_i\partial_j\ell_\xi]$ (2.8) or $4\int\partial_i\sqrt p\,\partial_j\sqrt p\,dx$ (2.10).
- It is symmetric positive semidefinite, and positive definite iff the scores $\partial_1\ell, \dots, \partial_n\ell$ are linearly independent; assuming this, $\langle\partial_i, \partial_j\rangle = g_{ij}$ is a Riemannian metric, the Fisher metric, and $\langle X, Y\rangle_\xi = E_\xi[(X\ell)(Y\ell)]$.
- Monotonicity (Theorem 2.1): any statistic $Y = F(X)$ loses information, $G_F(\xi) \le G(\xi)$, with loss $\Delta G = E[\text{Cov}(\partial_i\ell, \partial_j\ell \mid Y)]$, and no loss iff $F$ is sufficient.
- Additivity for independent observations, $G_{12} = G_1 + G_2$ (2.22), and convexity under mixing, $G_\lambda \le \lambda G_1 + (1 - \lambda)G_2$ (2.23).
- Cramer-Rao (Theorem 2.2): an unbiased estimator has covariance $V_\xi[\hat\xi] \ge G(\xi)^{-1}$; efficient estimators attaining it rarely exist, but the MLE attains it asymptotically.
- Geometrically, $G$ measures how fast the distribution changes with $\xi$: a large $G$ means the data discriminate nearby parameters well.

## Learning objectives

- Define the Fisher information matrix and prove the three expressions (2.6), (2.8), (2.10) agree.
- Explain why it defines a Riemannian metric that does not depend on the parametrisation.
- State and prove the monotonicity theorem and the factorisation characterisation of sufficiency.
- State additivity, convexity and the Cramer-Rao inequality, and explain asymptotic efficiency.
- Compute Fisher information for standard families and for coarse-grained data.

## Core concepts

### The Fisher information matrix

For an $n$-dimensional model $S = \{p_\xi\}$, the Fisher information matrix at $\xi$ is $G(\xi) = [g_{ij}(\xi)]$ with

$$
g_{ij}(\xi) = E_\xi[\partial_i\ell_\xi\,\partial_j\ell_\xi] = \int\partial_i\ell(x; \xi)\,\partial_j\ell(x; \xi)\,p(x; \xi)\,dx, \tag{2.6}
$$

$$
\ell_\xi(x) = \ell(x; \xi) = \log p(x; \xi). \tag{2.7}
$$

For $n = 1$ it is the Fisher information.
The book assumes the integral is finite and $g_{ij}$ is $C^\infty$ in $\xi$.
Rewriting (2.4) as

$$
E_\xi[\partial_i\ell] = 0 \tag{2.9}
$$

and differentiating once more gives the second form,

$$
g_{ij}(\xi) = -E_\xi[\partial_i\partial_j\ell_\xi], \tag{2.8}
$$

and substituting $\partial_i\ell = 2\partial_i\sqrt p/\sqrt p$ gives a third,

$$
g_{ij}(\xi) = 4\int\partial_i\sqrt{p(x; \xi)}\,\partial_j\sqrt{p(x; \xi)}\,dx, \tag{2.10}
$$

revisited in section 2.5 (the square-root embedding).

### Positive definiteness and the metric

$G(\xi)$ is symmetric, and for $c \in \mathbb{R}^n$

$$
c^\top G(\xi)c = \int\left\{\sum_ic^i\partial_i\ell(x; \xi)\right\}^2p(x; \xi)\,dx \ge 0, \tag{2.11}
$$

so it is positive semidefinite.
The book assumes it is positive definite, which is equivalent to the scores $\{\partial_1\ell_\xi, \dots, \partial_n\ell_\xi\}$ being linearly independent as functions of $x$, i.e. $\{\partial_1p_\xi, \dots, \partial_np_\xi\}$ independent (a local identifiability condition).
Then $g_{ij} = \langle\partial_i, \partial_j\rangle$ defines a Riemannian metric, the Fisher metric or information metric.
Since $g_{ij}$ transforms by (1.22) under reparametrisation, the metric itself does not depend on the coordinates, and

$$
\langle X, Y\rangle_\xi = E_\xi[(X\ell)(Y\ell)] \qquad (X, Y \in T_\xi(S)).
$$

When $\mathcal{X}$ is finite, $\mathcal{P}(\mathcal{X})$ is itself a model of dimension $\lvert\mathcal{X}\rvert - 1$ and every model on $\mathcal{X}$ is a submanifold of it; for infinite $\mathcal{X}$ this picture is only heuristic.

### Sufficient statistics

Let $F : \mathcal{X} \to \mathcal{Y}$ and let $q(y; \xi)$ be the distribution of $Y = F(X)$ under $p(x; \xi)$.
Define

$$
r(x; \xi) = \frac{p(x; \xi)}{q(F(x); \xi)}, \qquad p(x \mid y; \xi) = r(x; \xi)\delta_{F(x)}(y), \qquad \Pr(A \mid y; \xi) = \int_Ap(x \mid y; \xi)\,dx, \tag{2.12-2.14}
$$

so that $\int_{A \cap F^{-1}(B)}p(x; \xi)\,dx = \int_B\Pr(A \mid y; \xi)\,q(y; \xi)\,dy$ (2.15): $\Pr(A \mid y; \xi)$ is the conditional probability of $X \in A$ given $Y = y$.
$F$ is a sufficient statistic for $S$ if this conditional distribution does not depend on $\xi$, i.e. $r(x; \xi) = r(x)$, so

$$
p(x; \xi) = q(F(x); \xi)\,r(x). \tag{2.16}
$$

Everything that depends on $\xi$ is in the distribution of $Y$; given $Y$ one can simulate $X$ without knowing $\xi$.
The factorisation theorem: $F$ is sufficient iff $p(x; \xi) = s(F(x); \xi)\,t(x)$ for some functions $s$ and $t$ (2.17).

### Monotonicity: Theorem 2.1

**Theorem 2.1.** The Fisher information matrix $G_F(\xi) = [g^F_{ij}(\xi)]$ of the induced model $S_F = \{q(y; \xi)\}$ satisfies $G_F(\xi) \le G(\xi)$: $\Delta G(\xi) = G(\xi) - G_F(\xi)$ is positive semidefinite.
$G_F = G$ for all $\xi$ iff $F$ is sufficient.
The information loss from summarising $x$ into $y = F(x)$ is

$$
\Delta g_{ij}(\xi) = E_\xi[\partial_i\log r(X; \xi)\,\partial_j\log r(X; \xi)] = E_\xi\big[\text{Cov}_\xi[\partial_i\ell(X; \xi), \partial_j\ell(X; \xi) \mid Y]\big]. \tag{2.18}
$$

Proof sketch: differentiating $\int_Bq\,dy = \int_{F^{-1}(B)}p\,dx$ shows $\partial_i\log q(y; \xi) = E_\xi[\partial_i\ell(X; \xi) \mid y]$ (2.19).
With $\partial_i\ell = \partial_i\log q(F(x); \xi) + \partial_i\log r(x; \xi)$ (2.20), this gives $E_\xi[\partial_i\log r \mid F(X)] = 0$: $\partial_i\log r$ is orthogonal to every function of $F(X)$ under $\langle\langle\Phi, \Psi\rangle\rangle_\xi = E_\xi[\Phi(X)\Psi(X)]$ (2.21).
So $G = G_F + \Delta G$ is a Pythagorean decomposition, $\Delta G$ is a conditional covariance and hence positive semidefinite, and it vanishes iff $\partial_i\log r = 0$ for all $i$, which is sufficiency.

$G_F \le G$ is the monotonicity and $G = G_F + \Delta G$ the chain rule of Fisher information.
Both extend to any Markov kernel $\kappa(y \mid x)$ with $q(y; \xi) = \int\kappa(y \mid x)p(x; \xi)\,dx$; a deterministic $F$ is the case $\kappa(y \mid x) = \delta_{F(x)}(y)$.

### Additivity and convexity

For a product model $p_{12}(x_1, x_2; \xi) = p_1(x_1; \xi)p_2(x_2; \xi)$ (independent observations),

$$
G_{12}(\xi) = G_1(\xi) + G_2(\xi), \tag{2.22}
$$

so $N$ i.i.d. observations carry $NG(\xi)$.
For two models on the same $\mathcal{X}$ and $\Xi$ and their mixture $\lambda p_1 + (1 - \lambda)p_2$,

$$
G_\lambda(\xi) \le \lambda G_1(\xi) + (1 - \lambda)G_2(\xi), \qquad 0 \le \lambda \le 1, \tag{2.23}
$$

which follows from monotonicity (see (3.23) in section 3.2): the mixture is what you see if you forget the label saying which component generated $x$.

### The Cramer-Rao inequality

An estimator $\hat\xi = [\hat\xi^1, \dots, \hat\xi^n] : \mathcal{X} \to \mathbb{R}^n$ is unbiased if

$$
E_\xi[\hat\xi(X)] = \xi \qquad \forall \xi \in \Xi. \tag{2.24}
$$

Its mean squared error is the covariance matrix $V_\xi[\hat\xi] = [v^{ij}_\xi]$, $v^{ij}_\xi = E_\xi[(\hat\xi^i(X) - \xi^i)(\hat\xi^j(X) - \xi^j)]$.

**Theorem 2.2 (Cramer-Rao).** For any unbiased estimator, $V_\xi[\hat\xi] \ge G(\xi)^{-1}$, i.e. $V_\xi[\hat\xi] - G(\xi)^{-1}$ is positive semidefinite.

Section 2.5 gives a geometric proof.
An unbiased estimator with $V_\xi[\hat\xi] = G(\xi)^{-1}$ for all $\xi$ is efficient; it is then the best unbiased estimator, but the best unbiased estimator need not attain the bound, and biased estimators can have smaller mean squared error.
Efficient estimators exist only for special combinations of model and parametrisation (exponential families with expectation parameters, section 3.5).
However, there is always a sequence $\hat\xi_N = \hat\xi_N(x_1, \dots, x_N)$ that attains the bound asymptotically as $N \to \infty$ (for example the MLE), an asymptotically efficient or first-order efficient estimator (sections 4.1 and 4.4).
So $G(\xi)^{-1}$ is the scale of unavoidable estimation error: a larger $G$ means the distribution changes more when $\xi$ changes, and $\xi$ can be estimated more accurately.

## Worked examples

### The normal family

From $\partial_\mu\ell = (x - \mu)/\sigma^2$ and $\partial_\sigma\ell = (x - \mu)^2/\sigma^3 - 1/\sigma$, with $E[(x - \mu)^2] = \sigma^2$ and $E[(x - \mu)^4] = 3\sigma^4$:

$$
g_{\mu\mu} = \frac{1}{\sigma^2}, \qquad g_{\sigma\sigma} = \frac{3 - 2 + 1}{\sigma^2} = \frac{2}{\sigma^2}, \qquad g_{\mu\sigma} = 0
$$

(odd central moments vanish).
(2.8) gives the same matrix, and (2.10) evaluated numerically at $(\mu, \sigma) = (1, 2)$ gives $g_{\mu\mu} = 0.25$ and $g_{\sigma\sigma} = 0.5$.
This is the hyperbolic metric $(d\mu^2 + 2d\sigma^2)/\sigma^2$ of chapter 1.

### Bernoulli and Poisson

Bernoulli($p$): $\partial_p\ell = 1/p$ if $x = 1$ and $-1/(1 - p)$ if $x = 0$, so $g = p \cdot 1/p^2 + (1 - p) \cdot 1/(1 - p)^2 = 1/(p(1 - p))$, which is $4.7619$ at $p = 0.3$.
Poisson($\xi$): $\partial_\xi\ell = x/\xi - 1$, so $g = \text{Var}(x)/\xi^2 = 1/\xi$.
In both cases $1/g$ is the variance of one observation, and the sample mean of $N$ observations has variance $1/(Ng)$: it is efficient.

### Information lost by keeping only the sign

Observe $X \sim N(\mu, 1)$ ($G = 1$) but record only $Y = 1\{X > 0\}$, a Bernoulli with $P(Y = 1) = \Phi(\mu)$.
By the chain rule, $G_F(\mu) = \phi(\mu)^2/(\Phi(\mu)(1 - \Phi(\mu)))$.
At $\mu = 0$: $G_F = (1/2\pi)/(1/4) = 2/\pi = 0.6366$, so the loss is $\Delta G = 0.3634$; at $\mu = 1$, $G_F = 0.4386$.
Check with (2.18) at $\mu = 0$: the score is $X$, and given the sign, $X$ is half-normal with variance $1 - 2/\pi = 0.3634$, the same number.
"Thresholding throws away about 36% of the information at the threshold and more away from it."

### Convexity of mixtures

$p_1 = N(\xi, 1)$ has $G_1 = 1$ and $p_2 = N(\xi, 4)$ has $G_2 = 0.25$.
Their equal mixture has, by numerical integration at $\xi = 0$, $G_{1/2} = 0.4615$, below the bound $0.5 \cdot 1 + 0.5 \cdot 0.25 = 0.625$ from (2.23).

### An unbiased estimator that is not efficient

For $N$ observations from $N(\mu, v)$ with both unknown, the Fisher matrix in $(\mu, v)$ is $N\,\text{diag}(1/v, 1/(2v^2))$ (section 1.5 transformed), so the bound for $v$ is $2v^2/N$.
The unbiased sample variance $s^2$ has variance $2v^2/(N - 1)$: with $N = 10$ and $v = 1$, $0.2222 > 0.2$.
The sample mean attains its bound $v/N$ exactly.

## Pitfalls

- Using $-E[\partial_i\partial_j\ell]$ and $E[\partial_i\ell\,\partial_j\ell]$ interchangeably for a model where (2.4) fails (moving support), or replacing the expectation by the observed Hessian and calling it Fisher information.
- Forgetting that $G$ depends on the parametrisation through (1.22); "the Fisher information of the variance" and "of the standard deviation" differ by a Jacobian factor, while the metric is the same.
- Assuming the Cramer-Rao bound is attained; efficient estimators exist only in special cases, and the bound is asymptotic in general.
- Applying the bound to biased estimators; shrinkage estimators can beat $G^{-1}$ in mean squared error.
- Reading monotonicity as "any processing loses information"; sufficient statistics lose none, and the loss is a conditional variance that can be computed.

## Review questions

> [!question]- ig-fm-three-forms | Give three expressions for $g_{ij}(\xi)$.
> $E_\xi[\partial_i\ell\,\partial_j\ell]$, $-E_\xi[\partial_i\partial_j\ell]$, and $4\int\partial_i\sqrt p\,\partial_j\sqrt p\,dx$, with $\ell = \log p$. The second follows by differentiating $E_\xi[\partial_j\ell] = 0$.

> [!question]- ig-fm-pd | When is the Fisher matrix positive definite?
> $c^\top Gc = E[(c^i\partial_i\ell)^2] \ge 0$, with equality iff $c^i\partial_i\ell = 0$ almost surely. So $G$ is positive definite iff the scores $\partial_1\ell, \dots, \partial_n\ell$ are linearly independent.

> [!question]- ig-fm-normal | Derive the Fisher matrix of $N(\mu, \sigma^2)$ in $(\mu, \sigma)$.
> $\text{diag}(1/\sigma^2, 2/\sigma^2)$. $E[(x - \mu)^2/\sigma^4] = 1/\sigma^2$; $E[((x - \mu)^2/\sigma^3 - 1/\sigma)^2] = (3 - 2 + 1)/\sigma^2$; the cross term involves odd moments and vanishes.

> [!question]- ig-fm-monotonicity | State Theorem 2.1.
> For $Y = F(X)$, $G_F(\xi) \le G(\xi)$, with $\Delta G = E_\xi[\text{Cov}(\partial_i\ell, \partial_j\ell \mid Y)]$, and $G_F = G$ for all $\xi$ iff $F$ is sufficient.

> [!question]- ig-fm-sign | $X \sim N(\mu, 1)$ but only $1\{X > 0\}$ is recorded. Fisher information at $\mu = 0$?
> $2/\pi \approx 0.6366$, from $\phi(0)^2/(\Phi(0)(1 - \Phi(0))) = (1/2\pi)/(1/4)$. The loss $1 - 2/\pi$ equals the variance of the half-normal, as (2.18) predicts.

> [!question]- ig-fm-sufficient | What is a sufficient statistic, and what is the factorisation criterion?
> $F$ is sufficient if the conditional distribution of $X$ given $F(X)$ does not depend on $\xi$. Criterion: $p(x; \xi) = s(F(x); \xi)t(x)$.

> [!question]- ig-fm-additivity-convexity | What happens to Fisher information under independent pooling and under mixing?
> Independent observations add: $G_{12} = G_1 + G_2$. Mixtures are convex from below: $G_\lambda \le \lambda G_1 + (1 - \lambda)G_2$, since forgetting the component label is a loss of information.

> [!question]- ig-fm-cramer-rao | State the Cramer-Rao inequality and define efficiency.
> For unbiased $\hat\xi$, $V_\xi[\hat\xi] - G(\xi)^{-1}$ is positive semidefinite. $\hat\xi$ is efficient if equality holds for all $\xi$; the MLE is asymptotically efficient, $NV \to G^{-1}$.

> [!question]- ig-fm-s2 | Is the sample variance an efficient estimator of $v$ for normal data with unknown mean?
> No. Its variance is $2v^2/(N - 1)$ while the bound is $2v^2/N$ (for $N = 10$, $v = 1$: 0.2222 against 0.2). It is unbiased and asymptotically efficient.

> [!question]- ig-fm-invariance | Why is the Fisher metric independent of the parametrisation, even though $G$ changes?
> $G$ transforms as a $(0, 2)$ tensor, $\tilde G = J^\top GJ$, because scores transform by the chain rule $\tilde\partial_a\ell = (\partial \xi^i/\partial \rho^a)\partial_i\ell$. So $\langle X, Y\rangle = E[(X\ell)(Y\ell)]$ is coordinate-free.

## Where it leads

- [The Alpha-Connection](03-The-Alpha-Connection.md) adds a family of connections built from the same score functions.
- [Chentsov's Theorem](04-Chentsovs-Theorem-and-Some-Historical-Remarks.md): monotonicity under sufficient statistics singles out the Fisher metric.
- [The Geometry of P(X)](05-The-Geometry-of-P-of-X.md) proves Cramer-Rao geometrically, as a projection inequality.
- Code: [ch2_examples.py](code/ch2_examples.py).

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 2.2.
- C. R. Rao, "Information and the accuracy attainable in the estimation of statistical parameters", *Bulletin of the Calcutta Mathematical Society* 37 (1945), the origin of both the bound and the metric.
- Erich Lehmann and George Casella, *Theory of Point Estimation*, 2nd edition, chapters 2 (unbiasedness, information inequality) and 6 (asymptotic efficiency).
- Thomas Cover and Joy Thomas, *Elements of Information Theory*, 2nd edition, chapter 11 (Fisher information and the Cramer-Rao inequality).
