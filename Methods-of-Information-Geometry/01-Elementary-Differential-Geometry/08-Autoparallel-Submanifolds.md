---
type: concept
tier: core
status: solid
section: 1.8
pages: 19-22
prereqs: [flatness, submanifolds]
est_hours: 2.5
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.8, Kobayashi and Nomizu - Foundations of Differential Geometry vol 2 ch 7]
---

# Autoparallel Submanifolds

## TL;DR

- For $X, Y$ tangent to a submanifold $M$, $\nabla_XY$ is a vector of $T_p(S)$ but need not lie in $T_p(M)$.
- $M$ is autoparallel if $\nabla_XY \in \mathcal{T}(M)$ for all $X, Y \in \mathcal{T}(M)$ (1.50); equivalently $\nabla_{\partial_a}\partial_b = \Gamma^c_{ab}\partial_c$ (1.52), or $M$ is closed under parallel translation along curves in $M$.
- An autoparallel $M$ gets a connection by restriction, and its parallel translation is the restriction of that of $S$ (1.51); it inherits $R = 0$ and $T = 0$ from $S$.
- 1-dimensional autoparallel submanifolds are geodesics: $\frac{\delta}{dt}\frac{d\gamma}{dt} = 0$ in an affine parameter, i.e. $\ddot\gamma^k + \dot\gamma^i\dot\gamma^j\Gamma^k_{ij} = 0$ (1.56).
- Theorem 1.1: in a flat $S$, $M$ is autoparallel iff it is an affine subspace $\xi = Au + B$ in affine coordinates (1.57); geodesics are straight lines, and autoparallel submanifolds are flat.

## Learning objectives

- Compute $\nabla_XY$ for fields tangent to a submanifold and express it in the coordinates of $M$.
- State the equivalent forms of the autoparallel condition.
- Derive the geodesic equation and the notion of affine parameter.
- Prove Theorem 1.1 and use it to recognise autoparallel submanifolds of a flat space.

## Core concepts

### Covariant derivatives of tangent fields

Let $M \subset S$ with coordinates $[u^a]$ on $M$ and $[\xi^i]$ on $S$, $\partial_a = \partial/\partial u^a$, and let $\Gamma^k_{ij}$ be the coefficients of $\nabla$ on $S$.
For $X = X^a\partial_a$ and $Y = Y^a\partial_a$ tangent to $M$, define $\nabla_XY$ pointwise as $\nabla_{X_p}Y$ (as in 1.36).
Using $\partial_a = (\partial_a\xi^i)\partial_i$,

$$
\nabla_XY = X^a(\partial_aY^b)\partial_b + X^aY^b\{(\partial_a\xi^i)(\partial_b\xi^j)\Gamma^k_{ij} + \partial_a\partial_b\xi^k\}\partial_k, \tag{1.47}
$$

$$
\nabla_{\partial_a}\partial_b = \{(\partial_a\xi^i)(\partial_b\xi^j)\Gamma^k_{ij} + \partial_a\partial_b\xi^k\}\partial_k, \tag{1.48}
$$

$$
\nabla_XY = X^a(\partial_aY^b)\partial_b + X^aY^b\nabla_{\partial_a}\partial_b. \tag{1.49}
$$

$(\nabla_XY)_p \in T_p(S)$, but in general $\nabla_XY \notin \mathcal{T}(M)$.

### The autoparallel condition

If

$$
\nabla_XY \in \mathcal{T}(M) \qquad \forall X, Y \in \mathcal{T}(M), \tag{1.50}
$$

then $\nabla$ restricts to an affine connection on $M$ (properties (i)-(iv) of section 1.6 hold), and the parallel translation $\Pi^M_\gamma$ it defines along curves $\gamma$ in $M$ coincides with that of $S$:

$$
\Pi^M_\gamma = \Pi_\gamma\big|_{T_{\gamma(a)}(M)}. \tag{1.51}
$$

Such an $M$ is autoparallel with respect to $\nabla$; open subsets of $S$ are trivially autoparallel.
By (1.49), (1.50) holds iff $\nabla_{\partial_a}\partial_b \in \mathcal{T}(M)$ for all $a, b$, i.e. there are $m^3$ functions $\Gamma^c_{ab} \in \mathcal{F}(M)$ with

$$
\nabla_{\partial_a}\partial_b = \Gamma^c_{ab}\partial_c, \tag{1.52}
$$

which are then the connection coefficients on $M$; with (1.48) this is

$$
\Gamma^c_{ab}\partial_c\xi^k = (\partial_a\xi^i)(\partial_b\xi^j)\Gamma^k_{ij} + \partial_a\partial_b\xi^k. \tag{1.53}
$$

A third equivalent form: for every curve $\gamma$ in $M$ and every $D \in T_{\gamma(a)}(M)$, $\Pi_\gamma(D) \in T_{\gamma(b)}(M)$; parallel translation in $S$ never leaves the tangent spaces of $M$.

### Geodesics

1-dimensional autoparallel submanifolds are autoparallel curves or geodesics.
For a curve $\gamma$, (1.52) with (1.37) says

$$
\frac{\delta}{dt}\frac{d\gamma}{dt} = \Gamma(t)\frac{d\gamma}{dt} \tag{1.54}
$$

for some smooth function $\Gamma(t)$: the acceleration is along the velocity.
Since 1-dimensional connections are flat, a reparametrisation (an affine parameter) makes $\Gamma(t) \equiv 0$:

$$
\frac{\delta}{dt}\frac{d\gamma}{dt} = 0, \tag{1.55}
$$

so the velocity is parallel along $\gamma$; this is how geodesics are usually defined.
In coordinates, with $\gamma^i = \xi^i \circ \gamma$,

$$
\ddot\gamma^k(t) + \dot\gamma^i(t)\dot\gamma^j(t)(\Gamma^k_{ij})_{\gamma(t)} = 0. \tag{1.56}
$$

Only the symmetric part of $\Gamma$ enters (1.56), so torsion is invisible to geodesics.

### Inherited flatness and Theorem 1.1

If $T = 0$ on $S$ then $T = 0$ on an autoparallel $M$, from (1.46) and (1.53); similarly $R = 0$ on $S$ implies $R = 0$ on $M$ (from (1.45) and (1.53), or more simply from (1.51): if parallel translation in $S$ is path-independent, so is its restriction).
In a flat $S$ with affine coordinates $[\xi^i]$ and $M$ autoparallel, take $[u^a]$ affine on $M$ as well; (1.53) reduces to $\partial_a\partial_b\xi^k = 0$, i.e. there are an $n \times m$ matrix $A$ and $B \in \mathbb{R}^n$ with

$$
\xi(p) = Au(p) + B \qquad (\forall p \in M). \tag{1.57}
$$

A set $\{Au + B \mid u \in \mathbb{R}^m\}$ is an affine subspace of $\mathbb{R}^n$ (a linear subspace if $B = 0$).

**Theorem 1.1.** If $S$ is flat, a submanifold $M$ is autoparallel iff it is an affine subspace (or an open subset of one) of $S$ in an affine coordinate system.
In particular geodesics are straight lines (or segments) in affine coordinates, and an autoparallel submanifold of a flat space is itself flat.

## Worked examples

### A straight line in polar coordinates

The line $x = 1$, parametrised as $(1, t)$, is $r = \sqrt{1 + t^2}$, $\theta = \arctan t$ in polar coordinates.
With $\Gamma^r_{\theta\theta} = -r$ and $\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = 1/r$, (1.56) reads

$$
\ddot r - r\dot\theta^2 = 0, \qquad \ddot\theta + \frac{2}{r}\dot r\dot\theta = 0,
$$

and substituting $r(t)$ and $\theta(t)$ makes both sides vanish identically: Cartesian straight lines with linear parameter are geodesics, written in non-affine coordinates.

### A non-affine parameter

The same line as $(1, t^3)$ for $t > 0$ has velocity $(0, 3t^2)$ and acceleration $(0, 6t) = (2/t)(0, 3t^2)$.
This is (1.54) with $\Gamma(t) = 2/t$: still autoparallel (the image is a straight line), but $t$ is not an affine parameter; $s = t^3$ is.

### Planes and spheres in $\mathbb{R}^3$

With the flat connection, the plane $z = x + 2y + 1$ is $\xi = Au + B$ with $u = (x, y)$, $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 1 & 2\end{pmatrix}$ and $B = (0, 0, 1)$, so it is autoparallel by Theorem 1.1.
The unit sphere is not: for $\partial_\theta$ along a meridian, $\nabla_{\partial_\theta}\partial_\theta = \partial^2_\theta\xi = -\xi$, the inward radius, which is normal to the sphere and not in $T_p(M)$.
Great circles are geodesics of the sphere's own (projected) connection (section 1.9), not of $\mathbb{R}^3$.

### Preview: exponential families

In section 2.6 the $e$-connection $\nabla^{(1)}$ makes the space of positive distributions on a finite set flat with $\log p$ as affine coordinates; an exponential family $\log p(x; \theta) = C(x) + \theta^iF_i(x) - \psi(\theta)$ is then (up to normalisation) an affine subspace, hence $e$-autoparallel by Theorem 1.1.

## Pitfalls

- Thinking a submanifold that is "straight in some coordinates" is autoparallel; it must be straight in affine coordinates of the given connection (compare the ray $\sigma = \mu$ in the normal family, which is not $e$-autoparallel).
- Forgetting the $\partial_a\partial_b\xi^k$ term in (1.48); even in flat $S$ with $\Gamma = 0$, a curved embedding gives $\nabla_{\partial_a}\partial_b \neq 0$.
- Calling any curve with $\frac{\delta}{dt}\dot\gamma \parallel \dot\gamma$ a non-geodesic; it is a geodesic with a non-affine parameter.
- Assuming geodesics are shortest paths for an arbitrary connection; that needs the Riemannian connection of a metric ([Riemannian Connection](10-Riemannian-Connection.md)).
- Expecting an arbitrary submanifold to inherit a connection; without (1.50) one needs a projection (section 1.9).

## Review questions

> [!question]- ig-ap-definition | When is a submanifold $M$ autoparallel with respect to $\nabla$?
> When $\nabla_XY \in \mathcal{T}(M)$ for all $X, Y \in \mathcal{T}(M)$, equivalently $\nabla_{\partial_a}\partial_b = \Gamma^c_{ab}\partial_c$ for some functions on $M$, equivalently parallel translation along curves in $M$ maps $T(M)$ into $T(M)$.

> [!question]- ig-ap-nabla-ab | Write $\nabla_{\partial_a}\partial_b$ for $M \subset S$ in terms of the embedding and $\Gamma^k_{ij}$.
> $\{(\partial_a\xi^i)(\partial_b\xi^j)\Gamma^k_{ij} + \partial_a\partial_b\xi^k\}\partial_k$ (equation 1.48). The second term is present even if $\Gamma = 0$.

> [!question]- ig-ap-geodesic-eq | Write the geodesic equation in coordinates.
> $\ddot\gamma^k + \dot\gamma^i\dot\gamma^j\Gamma^k_{ij} = 0$ (equation 1.56), for an affine parameter. In general $\frac{\delta}{dt}\dot\gamma = \Gamma(t)\dot\gamma$, and a reparametrisation removes $\Gamma(t)$.

> [!question]- ig-ap-theorem-1-1 | State Theorem 1.1 and give its proof idea.
> In flat $S$, $M$ is autoparallel iff it is an affine subspace $\xi = Au + B$ in affine coordinates. With $\Gamma^k_{ij} = 0$ and affine coordinates on the (inherited-flat) $M$, (1.53) becomes $\partial_a\partial_b\xi^k = 0$.

> [!question]- ig-ap-inherit | What curvature and torsion does an autoparallel submanifold inherit?
> If $S$ has $R = 0$ or $T = 0$, so does $M$, because its connection is the restriction and its parallel translation is the restriction of that of $S$ (equation 1.51 and 1.53).

> [!question]- ig-ap-sphere | Is the unit sphere an autoparallel submanifold of Euclidean $\mathbb{R}^3$?
> No. $\nabla_{\partial_\theta}\partial_\theta = \partial_\theta^2\xi = -\xi$ points along the normal, not into $T_p(M)$. By Theorem 1.1 only (open pieces of) planes are autoparallel 2-dimensional submanifolds.

> [!question]- ig-ap-affine-parameter | The line $(1, t^3)$, $t > 0$: is it a geodesic of the plane, and is $t$ an affine parameter?
> It is autoparallel (acceleration $(0, 6t) = (2/t)\times$ velocity), but $t$ is not affine because $\Gamma(t) = 2/t \neq 0$. The parameter $s = t^3$ is affine.

> [!question]- ig-ap-torsion-invisible | Why does torsion not affect geodesics?
> In $\dot\gamma^i\dot\gamma^j\Gamma^k_{ij}$ the product $\dot\gamma^i\dot\gamma^j$ is symmetric, so only the symmetric part of $\Gamma$ contributes, and torsion is the antisymmetric part.

## Where it leads

- [Projection of Connections and Embedding Curvature](09-Projection-of-Connections-and-Embedding-Curvature.md) measures how far a submanifold is from autoparallel.
- [Alpha-Affine Manifolds and Alpha-Families](../02-Geometric-Structure-of-Statistical-Models/06-Alpha-Affine-Manifolds-and-Alpha-Families.md): exponential families are $e$-autoparallel and mixture families $m$-autoparallel in $\mathcal{P}(\mathcal{X})$.
- Code: [ch1_examples.py](code/ch1_examples.py) checks the polar geodesic equations symbolically.

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.8.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, volume 2, chapter 7 (submanifolds, totally geodesic submanifolds).
