---
type: concept
tier: core
status: solid
section: 1.9
pages: 22-23
prereqs: [autoparallel-submanifolds, riemannian-metrics]
est_hours: 2.5
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.9, Lee - Introduction to Riemannian Manifolds 2nd ed ch 8, do Carmo - Riemannian Geometry ch 6]
---

# Projection of Connections and Embedding Curvature

## TL;DR

- A non-autoparallel submanifold gets a connection by projecting: $(\nabla^{(\pi)}_XY)_p = \pi_p((\nabla_XY)_p)$ for a smooth family of projections $\pi_p : T_p(S) \to T_p(M)$ (1.58).
- With a metric the natural choice is the orthogonal projection (1.59); the coefficients of the first kind $\Gamma_{ij,k} = \langle\nabla_{\partial_i}\partial_j, \partial_k\rangle$ (1.60) then give $\Gamma^{(\pi)}_{ab,c}$ of $M$ directly (1.62).
- The embedding curvature (second fundamental form) is the normal part $H(X, Y) = \nabla_XY - \nabla^{(\pi)}_XY$ (1.63), with components $H_{ab\kappa} = \langle\nabla_{\partial_a}\partial_b, \partial_\kappa\rangle$ (1.64); $M$ is autoparallel iff $H = 0$.
- Two different curvatures: $R^{(\pi)}$ is the intrinsic curvature of $M$, $H$ describes how $M$ bends inside $S$. A cylinder in $\mathbb{R}^3$ has $R^{(\pi)} = 0$ but $H \neq 0$.
- In statistics, the embedding curvature of a model in its ambient exponential family drives higher-order efficiency of estimators and tests (chapter 4).

## Learning objectives

- Define the projected connection and verify that it is a connection.
- Compute $\Gamma_{ij,k}$ and its transformation law, and the projected coefficients $\Gamma^{(\pi)}_{ab,c}$.
- Define the embedding curvature $H$ and its components, and relate $H = 0$ to autoparallelism.
- Distinguish intrinsic curvature from embedding curvature with examples.

## Core concepts

### Projected connections

If $M \subset S$ is not autoparallel, $\nabla$ does not restrict to $M$.
Suppose at each $p \in M$ a linear map $\pi_p : T_p(S) \to T_p(M)$ is given with $\pi_p(D) = D$ for $D \in T_p(M)$ (a projection), depending smoothly on $p$.
Then

$$
(\nabla^{(\pi)}_XY)_p = \pi_p((\nabla_XY)_p) \qquad (X, Y \in \mathcal{T}(M)) \tag{1.58}
$$

defines a connection $\nabla^{(\pi)}$ on $M$, the projection of $\nabla$ onto $M$ with respect to $\pi$.
If $S$ has a Riemannian metric $g = \langle\,,\rangle$, take $\pi_p$ orthogonal: for all $D \in T_p(S)$ and $D' \in T_p(M)$,

$$
\langle\pi_p(D), D'\rangle_p = \langle D, D'\rangle_p, \tag{1.59}
$$

and call $\nabla^{(\pi)}$ the projection of $\nabla$ onto $M$ with respect to $g$.

### Coefficients of the first kind

Given $\nabla$ and $g$, lower the upper index of $\Gamma$:

$$
\Gamma_{ij,k} \overset{\text{def}}{=} \langle\nabla_{\partial_i}\partial_j, \partial_k\rangle = \Gamma^h_{ij}g_{hk}. \tag{1.60}
$$

These are another component description of the same $\nabla$, with transformation law (from (1.29) and (1.22))

$$
\tilde\Gamma_{rs,t} = \left\langle\nabla_{\tilde\partial_r}\tilde\partial_s, \tilde\partial_t\right\rangle = \left(\frac{\partial \xi^i}{\partial \rho^r}\frac{\partial \xi^j}{\partial \rho^s}\Gamma_{ij,k} + \frac{\partial^2\xi^h}{\partial \rho^r\partial \rho^s}g_{hk}\right)\frac{\partial \xi^k}{\partial \rho^t}. \tag{1.61}
$$

For the projection onto $M$ with coordinates $[u^a]$, let $\Gamma^{(\pi)}_{ab,c} = \langle\nabla^{(\pi)}_{\partial_a}\partial_b, \partial_c\rangle$.
Since $\partial_c$ is tangent to $M$, (1.59) lets us drop the projection, and with (1.48),

$$
\Gamma^{(\pi)}_{ab,c} = \langle\nabla_{\partial_a}\partial_b, \partial_c\rangle = \{(\partial_a\xi^i)(\partial_b\xi^j)\Gamma_{ij,k} + (\partial_a\partial_b\xi^j)g_{jk}\}(\partial_c\xi^k). \tag{1.62}
$$

The upper-index coefficients follow as $\Gamma^{(\pi)c}_{ab} = \Gamma^{(\pi)}_{ab,d}g^{dc}$, with $g^{dc}$ the inverse of the induced metric $g_{ab}$.
If $\nabla$ is symmetric, so is $\nabla^{(\pi)}$.

### Embedding curvature

The part of $\nabla_XY$ that the projection throws away is

$$
H(X, Y) \overset{\text{def}}{=} \nabla_XY - \nabla^{(\pi)}_XY, \qquad H(X, Y)_p = (\nabla_XY)_p - \pi_p((\nabla_XY)_p) \in [T_p(M)]^\perp. \tag{1.63}
$$

The autoparallel condition (1.50) is exactly $H(X, Y) = 0$ for all $X, Y$, i.e. $H = 0$.
$H(X, Y)$ is $\mathcal{F}$-bilinear in $X$ and $Y$ (the derivative terms are tangent and cancel), so $H$ is a kind of tensor field with values in the normal spaces (not a vector field on $M$).
It measures how far $M$ is from autoparallel, how "curved" $M$ is inside $S$: the embedding curvature, or Euler-Schouten curvature, of $M$ with respect to $\nabla$.
Given a basis $\{(\partial_a)_p\}$ of $T_p(M)$ and a basis $\{(\partial_\kappa)_p; m + 1 \le \kappa \le n\}$ of $[T_p(M)]^\perp$, its components are

$$
H_{ab\kappa} \overset{\text{def}}{=} \langle H(\partial_a, \partial_b), \partial_\kappa\rangle = \langle\nabla_{\partial_a}\partial_b, \partial_\kappa\rangle, \tag{1.64}
$$

and $H = 0 \iff H_{ab\kappa} = 0$ for all $a, b, \kappa$.

### Intrinsic versus embedding curvature

$M$ has its own Riemann-Christoffel curvature $R^{(\pi)}$ from $\nabla^{(\pi)}$: the "inherent curvature" of $M$.
$H$ describes the curvature of the arrangement of $M$ in $S$.
By section 1.8, if $S$ is flat and $H = 0$ then $R^{(\pi)} = 0$, but $R^{(\pi)} = 0$ does not imply $H = 0$.
The standard example is a cylinder in Euclidean $\mathbb{R}^3$: its intrinsic geometry is that of a flat sheet rolled up, so $R^{(\pi)} = 0$, but it is curved in $\mathbb{R}^3$, so $H \neq 0$.

## Worked examples

### The sphere of radius $a$

Embed $x(\theta, \varphi) = a(\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$ in Euclidean $\mathbb{R}^3$ ($\Gamma = 0$, $g = I$), with unit outward normal $n = x/a$.
By (1.64) with $\nabla_{\partial_a}\partial_b = \partial_a\partial_bx$:

$$
H_{\theta\theta n} = \langle\partial^2_\theta x, n\rangle = -a, \qquad H_{\varphi\varphi n} = -a\sin^2\theta, \qquad H_{\theta\varphi n} = 0.
$$

The induced metric is $\text{diag}(a^2, a^2\sin^2\theta)$, so $H_{abn} = -\frac1a g_{ab}$: both principal curvatures are $-1/a$ (the sign says $\nabla_XX$ points inward).
At $a = 2$, $\theta = \pi/3$: $H_{\theta\theta n} = -2$, $H_{\varphi\varphi n} = -2 \times 0.75 = -1.5$.

### The projected connection of the sphere

By (1.62) with $\Gamma_{ij,k} = 0$ and $g = I$, $\Gamma^{(\pi)}_{ab,c} = \langle\partial_a\partial_bx, \partial_cx\rangle$.
For example $\Gamma^{(\pi)}_{\varphi\varphi,\theta} = \langle\partial^2_\varphi x, \partial_\theta x\rangle = -a^2\sin\theta\cos\theta$.
This equals the Christoffel symbol of the first kind $\frac12(2\partial_\varphi g_{\varphi\theta} - \partial_\theta g_{\varphi\varphi})$ of the induced metric, an instance of a general fact: projecting the Euclidean connection orthogonally onto a submanifold gives the Riemannian connection of the induced metric ([Riemannian Connection](10-Riemannian-Connection.md)).

### The cylinder

$x(u, w) = (a\cos u, a\sin u, w)$ with normal $n = (\cos u, \sin u, 0)$.
Induced metric $\text{diag}(a^2, 1)$: constant, so all Christoffel symbols vanish and $R^{(\pi)} = 0$; $(au, w)$ are Euclidean coordinates on the cylinder.
Embedding curvature $H_{uun} = \langle\partial^2_ux, n\rangle = -a \neq 0$, $H_{uwn} = H_{wwn} = 0$: curved around, straight along.

### A circle in the plane

For the circle of radius $a$ with unit-speed parameter $s$, $\nabla_TT = \ddot x = -\frac1a n$; $\lvert H(T, T)\rvert = 1/a$ is the familiar curvature of a circle.
A 1-dimensional $M$ always has $R^{(\pi)} = 0$, so for curves all curvature is embedding curvature.

## Pitfalls

- Thinking the projected connection is canonical without a metric; it depends on the choice of projection, and different metrics give different projected connections.
- Treating $H$ as a vector field on $M$; its values are normal to $M$.
- Concluding from $R^{(\pi)} = 0$ that $M$ is autoparallel (cylinder), or from $H \neq 0$ that $M$ is intrinsically curved.
- Forgetting the second-derivative term in (1.61) and (1.62); $\Gamma_{ij,k}$ is not a tensor either.
- Assuming the projection of a non-metric connection is the Riemannian connection of the induced metric; that holds only when the ambient connection is metric (and torsion-free).

## Review questions

> [!question]- ig-emb-projection | How does a non-autoparallel submanifold get a connection from $S$?
> By projection: $(\nabla^{(\pi)}_XY)_p = \pi_p((\nabla_XY)_p)$ for a smooth family of projections $\pi_p : T_p(S) \to T_p(M)$, typically the orthogonal projection for a metric $g$.

> [!question]- ig-emb-first-kind | Define $\Gamma_{ij,k}$ and relate it to $\Gamma^k_{ij}$.
> $\Gamma_{ij,k} = \langle\nabla_{\partial_i}\partial_j, \partial_k\rangle = \Gamma^h_{ij}g_{hk}$: the coefficients with the upper index lowered by the metric. They need both $\nabla$ and $g$.

> [!question]- ig-emb-projected-coeffs | Give $\Gamma^{(\pi)}_{ab,c}$ for the orthogonal projection onto $M$.
> $\Gamma^{(\pi)}_{ab,c} = \langle\nabla_{\partial_a}\partial_b, \partial_c\rangle = \{(\partial_a\xi^i)(\partial_b\xi^j)\Gamma_{ij,k} + (\partial_a\partial_b\xi^j)g_{jk}\}\partial_c\xi^k$. The projection can be dropped because $\partial_c$ is tangent.

> [!question]- ig-emb-h-definition | Define the embedding curvature and its relation to autoparallelism.
> $H(X, Y) = \nabla_XY - \nabla^{(\pi)}_XY$, the component of $\nabla_XY$ normal to $M$, with components $H_{ab\kappa} = \langle\nabla_{\partial_a}\partial_b, \partial_\kappa\rangle$. $M$ is autoparallel iff $H = 0$.

> [!question]- ig-emb-cylinder | Why is a cylinder in $\mathbb{R}^3$ the standard example separating $R^{(\pi)}$ and $H$?
> Its induced metric $\text{diag}(a^2, 1)$ is constant, so its intrinsic curvature $R^{(\pi)}$ is 0 (it unrolls flat), but $H_{uun} = -a \neq 0$, so it is not autoparallel in $\mathbb{R}^3$.

> [!question]- ig-emb-sphere | What is the embedding curvature of a sphere of radius $a$ in $\mathbb{R}^3$?
> $H_{abn} = -\frac1ag_{ab}$ with the outward normal: both principal curvatures are $-1/a$. At $a = 2$, $\theta = \pi/3$: $H_{\theta\theta n} = -2$, $H_{\varphi\varphi n} = -1.5$.

> [!question]- ig-emb-h-tensorial | Why is $H$ $\mathcal{F}$-bilinear even though $\nabla$ is not?
> $\nabla_X(fY) = f\nabla_XY + (Xf)Y$ and the extra term $(Xf)Y$ is tangent to $M$, so it is removed by subtracting $\nabla^{(\pi)}_X(fY)$. The normal part is $f\,H(X, Y)$.

## Where it leads

- [Riemannian Connection](10-Riemannian-Connection.md): orthogonal projection of a metric connection gives the metric connection of the submanifold.
- [The Alpha-Connection](../02-Geometric-Structure-of-Statistical-Models/03-The-Alpha-Connection.md) and chapter 4: the $\alpha$-embedding curvatures (in particular the $e$-curvature, Efron's statistical curvature) of a curved exponential family control second-order loss of information.
- Code: [ch1_examples.py](code/ch1_examples.py).

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.9.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd edition, chapter 8 (the second fundamental form, Gauss formula).
- Manfredo do Carmo, *Riemannian Geometry*, chapter 6 (isometric immersions).
- Bradley Efron, "Defining the Curvature of a Statistical Problem (with Applications to Second Order Efficiency)", *Annals of Statistics* 3(6) (1975).
