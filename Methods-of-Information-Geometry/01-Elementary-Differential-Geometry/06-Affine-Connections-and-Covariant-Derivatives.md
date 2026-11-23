---
type: concept
tier: core
status: solid
section: 1.6
pages: 13-17
prereqs: [vector-fields-and-tensor-fields]
est_hours: 4
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.6, Lee - Introduction to Riemannian Manifolds 2nd ed ch 4, do Carmo - Riemannian Geometry ch 2]
---

# Affine Connections and Covariant Derivatives

## TL;DR

- Tangent spaces at different points are unrelated vector spaces; an affine connection is the extra structure that links $T_p$ and $T_{p'}$ for neighbouring points.
- Infinitesimally, $\Pi_{p,p'}((\partial_j)_p) = (\partial_j)_{p'} - d\xi^i(\Gamma^k_{ij})_p(\partial_k)_{p'}$ (1.27); the $n^3$ smooth functions $\Gamma^k_{ij}$ are the connection coefficients.
- $\Gamma^k_{ij}$ is not a tensor: a change of coordinates adds a second-derivative term (1.29), so $\Gamma$ can vanish in one coordinate system and not in another.
- Integrating along a curve gives parallel translation $\Pi_\gamma : T_{\gamma(a)} \to T_{\gamma(b)}$, a linear isomorphism defined by the ODE $\dot X^k + \dot\gamma^iX^j\Gamma^k_{ij} = 0$ (1.32); it depends on the curve in general.
- The covariant derivative $\nabla_XY = X^i(\partial_iY^k + Y^j\Gamma^k_{ij})\partial_k$ (1.38), with $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$ (1.39), is $\mathcal{F}$-linear in $X$ and a derivation in $Y$; properties (i)-(iv) can serve as the definition.
- Connections form an affine space: the difference of two connections is a $(1, 2)$ tensor, and $\alpha\nabla + (1 - \alpha)\nabla'$ is a connection for every real $\alpha$ (the origin of the $\alpha$-connections).

## Learning objectives

- Explain why comparing tangent vectors at different points needs extra structure.
- Define connection coefficients and derive their transformation law.
- Write and solve the parallel-translation equation along a curve.
- Define the covariant derivative along a curve and $\nabla_XY$, and compute them in coordinates.
- State the axioms (i)-(iv) and the affine-space structure of the set of connections.

## Core concepts

### Why a connection is needed

In an open set of $\mathbb{R}^n$ every $T_p$ is identified with $\mathbb{R}^n$ through (1.4), so vectors at different points can be compared.
On a general manifold $T_p$ and $T_q$ for $p \neq q$ are different spaces.
To compare them we add structure: for each $p$ and each neighbour $p'$ (with $d\xi^i = \xi^i(p') - \xi^i(p)$ infinitesimal, second-order terms ignored), a linear one-to-one map $\Pi_{p,p'} : T_p \to T_{p'}$ (Figure 1.4).

### Connection coefficients

$\Pi_{p,p'}$ is fixed by its value on the basis.
Assume $\Pi_{p,p'}((\partial_j)_p)$ differs from $(\partial_j)_{p'}$ by an infinitesimal that is linear in $d\xi$:

$$
\Pi_{p,p'}((\partial_j)_p) = (\partial_j)_{p'} - d\xi^i(\Gamma^k_{ij})_p(\partial_k)_{p'}. \tag{1.27}
$$

If the $n^3$ functions $p \mapsto (\Gamma^k_{ij})_p$ are $C^\infty$, they define an affine connection, and $\Gamma^k_{ij}$ are its connection coefficients with respect to $[\xi^i]$.
The only constraint is smoothness, so a connection has exactly this many degrees of freedom.
(Rigorously, connections are defined through fibre bundles; the book keeps the infinitesimal picture.)

### Transformation law: $\Gamma$ is not a tensor

In coordinates $[\rho^r]$ with $\tilde\partial_r = \partial/\partial \rho^r$, expanding $(\partial \xi^j/\partial \rho^s)_{p'}$ to first order and inserting into (1.27) gives

$$
\Pi_{p,p'}((\tilde\partial_s)_p) = (\tilde\partial_s)_{p'} - d\rho^r(\tilde\Gamma^t_{rs})_p(\tilde\partial_t)_{p'}, \tag{1.28}
$$

$$
\tilde\Gamma^t_{rs} = \left\{\Gamma^k_{ij}\frac{\partial \xi^i}{\partial \rho^r}\frac{\partial \xi^j}{\partial \rho^s} + \frac{\partial^2\xi^k}{\partial \rho^r\partial \rho^s}\right\}\frac{\partial \rho^t}{\partial \xi^k}. \tag{1.29}
$$

The first term is the $(1, 2)$ tensor law (1.16); the second term, built from second derivatives of the coordinate change, is why $\Gamma$ is not a tensor.
(1.27) and (1.28) have the same form, so the notion of connection is coordinate-free even though its coefficients are not.

### Parallel translation along a curve

Composing infinitesimal translations along a curve $\gamma : [a, b] \to S$ links $T_{\gamma(a)}$ and $T_{\gamma(b)}$.
A vector field along $\gamma$ is a map $t \mapsto X(t) \in T_{\gamma(t)}$; it is parallel if

$$
X(t + dt) = \Pi_{\gamma(t),\gamma(t+dt)}(X(t)) \tag{1.30}
$$

for every $t$ (Figure 1.5).
With $X(t) = X^k(t)(\partial_k)_{\gamma(t)}$ and $\dot\gamma^i = d(\xi^i \circ \gamma)/dt$, (1.27) gives

$$
\Pi_{\gamma(t),\gamma(t+dt)}(X(t)) = \{X^k(t) - dt\,\dot\gamma^i(t)X^j(t)(\Gamma^k_{ij})_{\gamma(t)}\}(\partial_k)_{\gamma(t+dt)}, \tag{1.31}
$$

and parallelism becomes the linear ODE

$$
\dot X^k(t) + \dot\gamma^i(t)X^j(t)(\Gamma^k_{ij})_{\gamma(t)} = 0. \tag{1.32}
$$

Given $X(a) = D$ there is a unique solution, and $\Pi_\gamma(D) = X(b)$ defines the parallel translation $\Pi_\gamma : T_p \to T_q$ along $\gamma$, a linear isomorphism.
It generally depends on $\gamma$, not only on its endpoints.

### Covariant derivative along a curve

$X(t + h)$ and $X(t)$ lie in different spaces, so $\lim(X(t + h) - X(t))/h$ is meaningless.
Translating $X(t + h)$ back to $T_{\gamma(t)}$ first fixes this:

$$
\frac{\delta X}{dt} = \lim_{h \to 0}\frac{\Pi_{\gamma(t+h),\gamma(t)}(X(t + h)) - X(t)}{h}, \qquad \delta X(t) = \Pi_{\gamma(t+dt),\gamma(t)}(X(t + dt)) - X(t). \tag{1.33}
$$

Using the inverse of (1.27) (Figure 1.6),

$$
\Pi_{\gamma(t+dt),\gamma(t)}(X(t + dt)) = \{X^k(t + dt) + dt\,\dot\gamma^i(t)X^j(t)(\Gamma^k_{ij})_{\gamma(t)}\}(\partial_k)_{\gamma(t)}, \tag{1.34}
$$

$$
\frac{\delta X(t)}{dt} = \{\dot X^k(t) + \dot\gamma^i(t)X^j(t)(\Gamma^k_{ij})_{\gamma(t)}\}(\partial_k)_{\gamma(t)}. \tag{1.35}
$$

So $X$ is parallel along $\gamma$ iff $\delta X/dt = 0$, and one could equally define parallel translation from $\delta X/dt$.

### The covariant derivative $\nabla_XY$

For a vector field $X = X^i\partial_i$ on $S$ and $D = D^i(\partial_i)_p$, take any curve through $p$ with velocity $D$ and differentiate along it:

$$
\nabla_DX = D^i\{(\partial_iX^k)_p + X^j_p(\Gamma^k_{ij})_p\}(\partial_k)_p \in T_p(S). \tag{1.36}
$$

This depends only on $D$, and for any curve, $\frac{\delta X_{\gamma(t)}}{dt} = \nabla_{\dot\gamma(t)}X$ (1.37).
For $X, Y \in \mathcal{T}(S)$, $(\nabla_XY)_p = \nabla_{X_p}Y$ defines the covariant derivative of $Y$ with respect to $X$:

$$
\nabla_XY = X^i\{\partial_iY^k + Y^j\Gamma^k_{ij}\}\partial_k, \tag{1.38}
$$

$$
\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k. \tag{1.39}
$$

(1.39) reads: $\Gamma^k_{ij}$ measures how the basis field $\partial_j$ changes when moved in the direction $\partial_i$.

### Axioms and the space of connections

$\nabla : \mathcal{T} \times \mathcal{T} \to \mathcal{T}$ satisfies, for $X, Y, Z \in \mathcal{T}$ and $f \in \mathcal{F}$:

1. $\nabla_{X+Y}Z = \nabla_XZ + \nabla_YZ$;
2. $\nabla_X(Y + Z) = \nabla_XY + \nabla_XZ$;
3. $\nabla_{fX}Y = f\nabla_XY$;
4. $\nabla_X(fY) = f\nabla_XY + (Xf)Y$.

$\nabla_XY$ is $\mathcal{F}$-linear in $X$ but not in $Y$, so $\nabla$ is not a tensor.
These four properties can serve as the definition of a connection; one then defines $\Gamma^k_{ij}$ by (1.39), proves (1.38) and (1.29), and derives parallel translation, avoiding infinitesimals and fibre bundles.
The book calls the connection $\nabla$.

The set of connections is an affine space: for connections $\nabla, \nabla'$ and any $\alpha \in \mathbb{R}$, $\alpha\nabla + (1 - \alpha)\nabla'$ is a connection, and $\nabla - \nabla'$ is a tensor field of type $(1, 2)$ (the inhomogeneous term of (1.29) cancels in the difference, and property 4 does too).

## Worked examples

### Polar coefficients of the flat connection

The Euclidean connection has $\Gamma^k_{ij} = 0$ in Cartesian coordinates $(x, y)$.
(1.29) with $\Gamma = 0$ leaves $\tilde\Gamma^t_{rs} = \frac{\partial^2\xi^k}{\partial \rho^r\partial \rho^s}\frac{\partial \rho^t}{\partial \xi^k}$, and with $x = r\cos\theta$, $y = r\sin\theta$:

$$
\tilde\Gamma^r_{\theta\theta} = -r, \qquad \tilde\Gamma^\theta_{r\theta} = \tilde\Gamma^\theta_{\theta r} = \frac1r, \qquad \text{others } 0.
$$

For example $\partial^2(x, y)/\partial \theta^2 = (-r\cos\theta, -r\sin\theta) = -r\,\partial_r$ in vector terms, so $\nabla_{\partial_\theta}\partial_\theta = -r\partial_r$: moving around a circle, the basis vector $\partial_\theta$ turns inward.
"Same connection, zero coefficients in one chart and non-zero in another: that is what 'not a tensor' means."

### Parallel translation around a circle

Translate $X(0) = \partial_r$ along $r = 2$, $\theta = t$ with the coefficients above.
With $\dot\gamma = (0, 1)$, (1.32) is $\dot X^r - 2X^\theta = 0$, $\dot X^\theta + X^r/2 = 0$, solved by $X^r = \cos t$, $X^\theta = -\tfrac12\sin t$.
After a quarter turn, $X^r = 0$ and $X^\theta = -0.5$, i.e. $X = -0.5\,\partial_\theta$.
At $\theta = \pi/2$, $\partial_\theta = (-2, 0)$ in Cartesian terms, so $X = (1, 0)$: the original vector $\partial_r|_{\theta=0} = (1, 0)$, unchanged, as Euclidean parallelism requires.
The components moved only because the polar basis rotates.

### The difference of two connections is a tensor

On $\mathbb{R}^2$ let $\nabla$ be the flat connection and $\nabla'$ have constant Cartesian coefficients $\Gamma'^1_{12} = 1$, others 0.
Then $(\nabla' - \nabla)_XY = X^1Y^2\partial_1$, which is $\mathcal{F}$-linear in both $X$ and $Y$: a $(1, 2)$ tensor.
Section 2.3 builds the $\alpha$-connections exactly this way, as $\nabla^{(0)}$ plus a multiple of a fixed tensor.

## Pitfalls

- Treating $\Gamma^k_{ij}$ as a tensor and concluding a connection is "zero" because its coefficients vanish in one chart, or "non-zero" because they do not vanish in another.
- Differentiating components and calling it the covariant derivative; $\dot X^k$ alone is not coordinate-free, the $\Gamma$ term is what makes $\delta X/dt$ a vector.
- Assuming parallel translation depends only on endpoints; it does only for a flat connection on a simply connected space ([Flatness](07-Flatness.md)).
- Forgetting that a connection is independent of any metric; nothing in this section uses $g$, and the connections of statistics are often not the metric one ([Riemannian Connection](10-Riemannian-Connection.md)).
- Mixing index conventions; the book puts the direction of differentiation first, $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$, which matters once $\Gamma^k_{ij} \neq \Gamma^k_{ji}$.

## Review questions

> [!question]- ig-conn-why | Why does a manifold need an affine connection before you can differentiate vector fields?
> A derivative compares $X$ at nearby points, but $T_p$ and $T_{p'}$ are different vector spaces with no natural identification. A connection supplies the linear maps $\Pi_{p,p'}$ that make the comparison possible.

> [!question]- ig-conn-coefficients | How are the connection coefficients defined from $\nabla$?
> $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$ (equation 1.39), equivalently $\Pi_{p,p'}((\partial_j)_p) = (\partial_j)_{p'} - d\xi^i\Gamma^k_{ij}(\partial_k)_{p'}$.

> [!question]- ig-conn-not-tensor | Show that connection coefficients are not a tensor.
> Under a coordinate change, $\tilde\Gamma^t_{rs} = \{\Gamma^k_{ij}(\partial \xi^i/\partial \rho^r)(\partial \xi^j/\partial \rho^s) + \partial^2\xi^k/\partial \rho^r\partial \rho^s\}\partial \rho^t/\partial \xi^k$. The second-derivative term is absent from the tensor law; for example the flat connection has $\Gamma = 0$ in Cartesian and $\Gamma^r_{\theta\theta} = -r$ in polar.

> [!question]- ig-conn-parallel-ode | Write the equation for parallel translation of $X$ along $\gamma$.
> $\dot X^k + \dot\gamma^iX^j\Gamma^k_{ij} = 0$ (equation 1.32), a linear ODE, so a unique parallel field exists for each initial vector and $\Pi_\gamma$ is a linear isomorphism.

> [!question]- ig-conn-nabla-coords | Write $\nabla_XY$ in coordinates.
> $\nabla_XY = X^i(\partial_iY^k + Y^j\Gamma^k_{ij})\partial_k$ (equation 1.38).

> [!question]- ig-conn-axioms | List the four properties that characterise an affine connection $\nabla$.
> Additive in $X$ and in $Y$; $\nabla_{fX}Y = f\nabla_XY$; $\nabla_X(fY) = f\nabla_XY + (Xf)Y$. So it is $\mathcal{F}$-linear in $X$ and a derivation in $Y$.

> [!question]- ig-conn-difference | Why is the difference of two connections a tensor?
> In $\nabla_X(fY) - \nabla'_X(fY)$ the $(Xf)Y$ terms cancel, so the difference is $\mathcal{F}$-linear in both slots: a $(1, 2)$ tensor. Equivalently the second-derivative terms in (1.29) cancel.

> [!question]- ig-conn-affine-space | Is $\alpha\nabla + (1 - \alpha)\nabla'$ a connection for every real $\alpha$, including $\alpha$ outside $[0, 1]$?
> Yes. Properties 1-3 are linear and in property 4 the $(Xf)Y$ terms add up to $(\alpha + 1 - \alpha)(Xf)Y$. Connections form an affine space, which is what lets section 2.3 define $\nabla^{(\alpha)}$ for all real $\alpha$.

> [!question]- ig-conn-polar-transport | Transport $\partial_r$ a quarter turn along the circle $r = 2$. What are the polar components, and what vector is it?
> $X^r = 0$, $X^\theta = -0.5$; since $\partial_\theta = (-2, 0)$ at $\theta = \pi/2$, $X = (1, 0)$, the starting vector. The flat connection does not rotate vectors; only the polar basis rotated.

## Where it leads

- [Flatness](07-Flatness.md): when can coordinates be chosen with $\Gamma = 0$?
- [The Alpha-Connection](../02-Geometric-Structure-of-Statistical-Models/03-The-Alpha-Connection.md) defines a one-parameter family of connections on statistical models.
- Code: [ch1_examples.py](code/ch1_examples.py) derives the polar coefficients from (1.29) and integrates (1.32) numerically.

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.6.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd edition, chapter 4 (connections, covariant derivatives along curves, parallel transport).
- Manfredo do Carmo, *Riemannian Geometry*, chapter 2.
