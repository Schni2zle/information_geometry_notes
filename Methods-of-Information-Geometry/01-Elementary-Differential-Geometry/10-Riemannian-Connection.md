---
type: concept
tier: core
status: solid
section: 1.10
pages: 23-24
prereqs: [riemannian-metrics, flatness, projection-of-connections-and-embedding-curvature]
est_hours: 3
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.10, Lee - Introduction to Riemannian Manifolds 2nd ed ch 5 and 6, Costa Santos and Strapasson - Fisher Information Distance (Discrete Applied Mathematics 2015)]
---

# Riemannian Connection

## TL;DR

- $\nabla$ is metric with respect to $g$ if $Z\langle X, Y\rangle = \langle\nabla_ZX, Y\rangle + \langle X, \nabla_ZY\rangle$ (1.65), i.e. $\partial_kg_{ij} = \Gamma_{ki,j} + \Gamma_{kj,i}$ (1.66).
- Metric connections are exactly those whose parallel translation preserves inner products: $\langle\Pi_\gamma D_1, \Pi_\gamma D_2\rangle_q = \langle D_1, D_2\rangle_p$ (1.68).
- There is exactly one connection that is both metric and symmetric, the Riemannian (Levi-Civita) connection, with $\Gamma_{ij,k} = \frac12(\partial_ig_{jk} + \partial_jg_{ki} - \partial_kg_{ij})$ (1.69).
- Its geodesics are locally the shortest curves for the length (1.25).
- It is flat iff a Euclidean coordinate system $\langle\partial_i, \partial_j\rangle = \delta_{ij}$ exists (1.70).
- Ordinary differential geometry uses only this connection; statistical manifolds naturally carry non-metric connections, and that leads to dual connections (chapter 3).

## Learning objectives

- Define metric connections and prove that they preserve inner products under parallel translation.
- Derive the Christoffel formula (1.69) and the uniqueness of the Levi-Civita connection.
- Compute Christoffel symbols, geodesics and curvature for concrete metrics, including the Fisher metric of the normal family.
- Characterise flat Riemannian connections by Euclidean coordinates.
- Explain why information geometry needs connections other than the Levi-Civita one.

## Core concepts

### Metric connections

Let $(S, g)$ be Riemannian and $\nabla$ a connection.
$\nabla$ is a metric connection with respect to $g$ if for all $X, Y, Z \in \mathcal{T}(S)$

$$
Z\langle X, Y\rangle = \langle\nabla_ZX, Y\rangle + \langle X, \nabla_ZY\rangle. \tag{1.65}
$$

In coordinates, with $\Gamma_{ij,k} = \langle\nabla_{\partial_i}\partial_j, \partial_k\rangle$ from (1.60),

$$
\partial_kg_{ij} = \Gamma_{ki,j} + \Gamma_{kj,i}. \tag{1.66}
$$

### Parallel translation is an isometry

For vector fields $X(t)$, $Y(t)$ along a curve $\gamma$, (1.65) gives

$$
\frac{d}{dt}\langle X(t), Y(t)\rangle = \left\langle\frac{\delta X(t)}{dt}, Y(t)\right\rangle + \left\langle X(t), \frac{\delta Y(t)}{dt}\right\rangle. \tag{1.67}
$$

If both are parallel, the right side is 0 and $\langle X(t), Y(t)\rangle$ is constant.
So for $\gamma$ from $p$ to $q$ and $D_1, D_2 \in T_p$,

$$
\langle\Pi_\gamma(D_1), \Pi_\gamma(D_2)\rangle_q = \langle D_1, D_2\rangle_p. \tag{1.68}
$$

Parallel translation is a metric isomorphism: lengths and angles are preserved, though the vector may rotate.

### The Levi-Civita connection

A connection that is metric and symmetric is the Riemannian connection or Levi-Civita connection of $g$, and it exists and is unique.
Write (1.66) three times with cyclically permuted indices and use $\Gamma_{ij,k} = \Gamma_{ji,k}$:

$$
\partial_ig_{jk} + \partial_jg_{ki} - \partial_kg_{ij} = (\Gamma_{ij,k} + \Gamma_{ik,j}) + (\Gamma_{jk,i} + \Gamma_{ji,k}) - (\Gamma_{ki,j} + \Gamma_{kj,i}) = 2\Gamma_{ij,k},
$$

so

$$
\Gamma_{ij,k} = \frac12(\partial_ig_{jk} + \partial_jg_{ki} - \partial_kg_{ij}). \tag{1.69}
$$

These are the Christoffel symbols (of the first kind); $\Gamma^k_{ij} = \Gamma_{ij,h}g^{hk}$.
The derivation shows uniqueness, and defining $\Gamma$ by (1.69) shows existence.

### Geodesics as shortest paths

The geodesics of the Riemannian connection locally coincide with the shortest curves joining two points, length measured by (1.25).
They also have constant speed $\lVert\dot\gamma\rVert$ in an affine parameter, by (1.68) applied to $\dot\gamma$ itself.
The geodesic distance between two points is the infimum of the lengths of curves joining them.

### Flatness and Euclidean coordinates

If the Riemannian connection is flat, take affine coordinates $[\xi^i]$: each $\partial_i$ is parallel, so by (1.68) $\langle\partial_i, \partial_j\rangle$ is constant on $S$.
Using the affine freedom (1.41) to orthonormalise, there is an affine coordinate system with

$$
\langle\partial_i, \partial_j\rangle = \delta_{ij}. \tag{1.70}
$$

Such a coordinate system is Euclidean with respect to $g$.
So the Riemannian connection is flat iff a Euclidean coordinate system exists; then $(S, g)$ is locally isometric to $\mathbb{R}^n$.

### Why statistics needs more

Most differential geometry uses only the Riemannian connection on a Riemannian manifold, and non-metric connections are seldom discussed.
On families of probability distributions, however, the natural connections (the $e$- and $m$-connections of section 2.3) are not metric, and that leads to the new notion of dual connections in chapter 3: a pair $(\nabla, \nabla^*)$ satisfying $Z\langle X, Y\rangle = \langle\nabla_ZX, Y\rangle + \langle X, \nabla^*_ZY\rangle$, of which (1.65) is the self-dual case $\nabla = \nabla^*$.

## Worked examples

### The unit sphere

With $g = \text{diag}(1, \sin^2\theta)$, (1.69) and raising the index give

$$
\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta, \qquad \Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta, \qquad \text{others } 0.
$$

These match the projected coefficients in [Projection of Connections and Embedding Curvature](09-Projection-of-Connections-and-Embedding-Curvature.md) at $a = 1$, and the equator $\theta = \pi/2$ satisfies the geodesic equation because $\Gamma^\theta_{\varphi\varphi} = 0$ there.

### Holonomy around a latitude

Parallel-translate $\partial_\theta$ once around the latitude $\theta_0 = \pi/3$ ($\gamma(t) = (\theta_0, t)$, $t \in [0, 2\pi]$).
(1.32) gives $\dot X^\theta = \sin\theta_0\cos\theta_0X^\varphi$ and $\dot X^\varphi = -\cot\theta_0X^\theta$, a rotation at angular rate $\cos\theta_0$ in the orthonormal frame $(\partial_\theta, \partial_\varphi/\sin\theta_0)$.
After one loop the vector has turned by $2\pi\cos\theta_0 = \pi$, so it returns as $-\partial_\theta$; numerical integration gives $X = (-1.000000, 0.000000)$ with squared length $1.000000$ preserved, as (1.68) requires.
The rotation relative to the starting vector equals the enclosed area $2\pi(1 - \cos\theta_0) = \pi$ modulo $2\pi$ (Gauss-Bonnet with curvature 1).
"A loop on a flat surface gives no rotation; here the vector reverses, which proves the sphere is curved and parallel translation path-dependent."

### The normal family as a hyperbolic plane

The Fisher metric of $N(\mu, \sigma^2)$ is $g = \text{diag}(1/\sigma^2, 2/\sigma^2)$ (section 2.2).
(1.69) gives

$$
\Gamma^\mu_{\mu\sigma} = \Gamma^\mu_{\sigma\mu} = -\frac1\sigma, \qquad \Gamma^\sigma_{\mu\mu} = \frac{1}{2\sigma}, \qquad \Gamma^\sigma_{\sigma\sigma} = -\frac1\sigma, \qquad \text{others } 0.
$$

(1.45) then gives Gaussian curvature $-1/2$: the normal family with the Fisher metric is a hyperbolic plane of constant negative curvature (the substitution $\mu = \sqrt2u$ turns it into twice the Poincare half-plane metric, $2(du^2 + d\sigma^2)/\sigma^2$).
The vertical line $\mu = 0$ is a geodesic: $\sigma(s) = e^{s/\sqrt2}$ satisfies $\ddot\sigma + \Gamma^\sigma_{\sigma\sigma}\dot\sigma^2 = 0$ with unit speed, so the Fisher-Rao distance from $N(0, 1)$ to $N(0, 4)$ is $\sqrt2\ln2 = 0.9803$.
Other geodesics are half-ellipses centred on the $\mu$-axis (half-circles in the $(u, \sigma)$ coordinates).

### Polar coordinates are not Euclidean but the plane is

The polar coefficients $\Gamma^r_{\theta\theta} = -r$, $\Gamma^\theta_{r\theta} = 1/r$ come out of (1.69) from $g = \text{diag}(1, r^2)$, the same as from (1.29).
The connection is flat, and a Euclidean coordinate system (1.70) exists: Cartesian coordinates.
The normal family has curvature $-1/2 \neq 0$, so no reparametrisation of $(\mu, \sigma)$ makes the Fisher metric the identity matrix everywhere.

## Pitfalls

- Assuming the connection of a Riemannian manifold must be the Levi-Civita one; the metric and the connection are independent structures, and statistics uses non-metric ones.
- Forgetting the symmetric hypothesis; metric connections with torsion exist, and uniqueness needs both conditions.
- Mixing up $\Gamma_{ij,k}$ and $\Gamma^k_{ij}$ when computing; (1.69) gives the first kind, and raising with $g^{hk}$ is a separate step.
- Treating "flat" and "Euclidean coordinates exist" as equivalent for a non-metric connection; (1.70) is special to the Riemannian connection, and a flat non-metric connection has affine coordinates in which $g_{ij}$ is not constant (chapter 3's dually flat spaces).
- Expecting geodesics to be globally shortest; on the sphere a geodesic arc longer than $\pi$ is not.

## Review questions

> [!question]- ig-lc-metric-def | When is a connection metric with respect to $g$, in invariant and in coordinate form?
> $Z\langle X, Y\rangle = \langle\nabla_ZX, Y\rangle + \langle X, \nabla_ZY\rangle$ for all fields, equivalently $\partial_kg_{ij} = \Gamma_{ki,j} + \Gamma_{kj,i}$.

> [!question]- ig-lc-isometry | Show that a metric connection preserves inner products under parallel translation.
> For parallel $X(t), Y(t)$ along $\gamma$, $\frac{d}{dt}\langle X, Y\rangle = \langle\delta X/dt, Y\rangle + \langle X, \delta Y/dt\rangle = 0$, so $\langle\Pi_\gamma D_1, \Pi_\gamma D_2\rangle = \langle D_1, D_2\rangle$.

> [!question]- ig-lc-christoffel | Derive the Christoffel formula for the Levi-Civita connection.
> Add the metric condition for $(i, j, k)$ and $(j, k, i)$, subtract it for $(k, i, j)$, and use symmetry $\Gamma_{ij,k} = \Gamma_{ji,k}$: $\Gamma_{ij,k} = \frac12(\partial_ig_{jk} + \partial_jg_{ki} - \partial_kg_{ij})$. This proves uniqueness; defining $\Gamma$ this way proves existence.

> [!question]- ig-lc-euclidean-coords | When is the Riemannian connection flat?
> Iff there is a Euclidean coordinate system, $\langle\partial_i, \partial_j\rangle = \delta_{ij}$. Affine coordinates have parallel $\partial_i$, so $g_{ij}$ is constant by metricity, and an affine change orthonormalises it.

> [!question]- ig-lc-sphere-symbols | Give the non-zero Christoffel symbols of the unit sphere in $(\theta, \varphi)$.
> $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$ and $\Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta$.

> [!question]- ig-lc-holonomy | Parallel-translate a vector once around the latitude $\theta_0 = \pi/3$ of the unit sphere. What comes back?
> The vector rotated by $2\pi\cos\theta_0 = \pi$, i.e. reversed; the deficit from a full turn, $2\pi(1 - \cos\theta_0) = \pi$, is the enclosed area times the curvature 1. Its length is unchanged.

> [!question]- ig-lc-normal-curvature | What is the Gaussian curvature of the normal family under the Fisher metric, and what is the Fisher-Rao distance from $N(0, 1)$ to $N(0, 4)$?
> $-1/2$: a hyperbolic plane. The line $\mu = 0$ is a geodesic, so the distance is $\int_1^2\sqrt2/\sigma\,d\sigma = \sqrt2\ln2 \approx 0.9803$.

> [!question]- ig-lc-why-nonmetric | Why does information geometry go beyond the Levi-Civita connection?
> The natural connections on statistical models, the exponential and mixture ($e$ and $m$) connections, are not metric. They are flat in natural and expectation parameters and are dual to each other with respect to the Fisher metric, which is the structure developed in chapter 3.

## Where it leads

- [The Alpha-Connection](../02-Geometric-Structure-of-Statistical-Models/03-The-Alpha-Connection.md): the Levi-Civita connection of the Fisher metric is $\nabla^{(0)}$, the midpoint of the $e$- and $m$-connections.
- [The Geometry of P(X)](../02-Geometric-Structure-of-Statistical-Models/05-The-Geometry-of-P-of-X.md): under the Fisher metric the probability simplex is a piece of a sphere, curved for $\nabla^{(0)}$ but flat for $\nabla^{(\pm1)}$.
- Code: [ch1_examples.py](code/ch1_examples.py) computes the symbols, the curvature $-1/2$ and the holonomy numerically.

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.10.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd edition, chapters 5 (the Levi-Civita connection) and 6 (geodesics and distance).
- Sueli I. R. Costa, Sandra A. Santos and Joao E. Strapasson, "Fisher information distance: a geometrical reading", *Discrete Applied Mathematics* 197 (2015), for the hyperbolic geometry of the normal family.
