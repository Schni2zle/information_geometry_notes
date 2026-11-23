---
type: concept
tier: core
status: solid
section: 1.5
pages: 11-12
prereqs: [vector-fields-and-tensor-fields, submanifolds]
est_hours: 2
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.5, Lee - Introduction to Riemannian Manifolds 2nd ed ch 2]
---

# Riemannian Metrics

## TL;DR

- A Riemannian metric $g = \langle\,,\rangle$ is a smooth choice of inner product (bilinear, symmetric, positive definite) on every $T_p(S)$; it is a $(0, 2)$ tensor field.
- A manifold does not come with a metric; there are infinitely many, and one must be chosen. On a statistical model there is a natural one, the Fisher metric (section 2.2).
- In coordinates $g_{ij} = \langle\partial_i, \partial_j\rangle$, $\langle D, D'\rangle = g_{ij}D^iD'^j$, and $G = [g_{ij}]$ is symmetric positive definite.
- Components transform as a $(0, 2)$ tensor (1.22); the inverse $g^{ij}$ transforms with the opposite Jacobians (1.24).
- Curve length is $\int\sqrt{g_{ij}\dot\gamma^i\dot\gamma^j}\,dt$ (1.25), and a submanifold inherits $g_{ab} = g_{ij}B^i_aB^j_b$ (1.26).

## Learning objectives

- Define a Riemannian metric and a Riemannian manifold $(S, g)$.
- Write the metric in components, raise and lower indices with $g_{ij}$ and $g^{ij}$, and transform both under coordinate changes.
- Compute lengths of curves.
- Compute the metric induced on a submanifold.

## Core concepts

### Inner products on tangent spaces

Suppose each $T_p(S)$ has an inner product $\langle\,,\rangle_p$:

$$
\langle aD + bD', D''\rangle_p = a\langle D, D''\rangle_p + b\langle D', D''\rangle_p \quad \text{(linearity)}, \tag{1.19}
$$

$$
\langle D, D'\rangle_p = \langle D', D\rangle_p \quad \text{(symmetry)}, \tag{1.20}
$$

$$
D \neq 0 \implies \langle D, D\rangle_p > 0 \quad \text{(positive definiteness)}. \tag{1.21}
$$

By (1.19)-(1.20), $\langle\,,\rangle_p \in [T_p(S)]^0_2$, so $g : p \mapsto \langle\,,\rangle_p$ is a tensor field of type $(0, 2)$.
When it is $C^\infty$ it is a Riemannian metric, and $(S, g)$ is a Riemannian manifold.
The metric is extra structure: the manifold alone does not determine it.

### Components

With respect to $[\xi^i]$, $g_{ij}(p) = \langle(\partial_i)_p, (\partial_j)_p\rangle_p$, and for $D = D^i\partial_i$, $D' = D'^j\partial_j$,

$$
\langle D, D'\rangle_p = g_{ij}(p)D^iD'^j, \qquad \lVert D\rVert^2 = g_{ij}D^iD^j.
$$

The matrix $G(p) = [g_{ij}(p)]$ is symmetric positive definite.
Conversely, any $n^2$ smooth functions $g_{ij}$ forming a symmetric positive definite matrix at every point define a unique Riemannian metric with those components.

### Transformation laws and the inverse metric

As a $(0, 2)$ tensor (compare (1.15)), with $\tilde g_{k\ell} = \langle\tilde\partial_k, \tilde\partial_\ell\rangle$ for $\tilde\partial_k = \partial/\partial \rho^k$:

$$
\tilde g_{k\ell} = g_{ij}\frac{\partial \xi^i}{\partial \rho^k}\frac{\partial \xi^j}{\partial \rho^\ell}, \qquad g_{ij} = \tilde g_{k\ell}\frac{\partial \rho^k}{\partial \xi^i}\frac{\partial \rho^\ell}{\partial \xi^j}. \tag{1.22}
$$

In matrix form $\tilde G = J^\top GJ$ with $J = \partial \xi/\partial \rho$.
Let $g^{ij}$ be the entries of $G^{-1}$, so

$$
g_{ij}g^{jk} = \delta^k_i. \tag{1.23}
$$

The inverse transforms with the other Jacobian:

$$
\tilde g^{k\ell} = g^{ij}\frac{\partial \rho^k}{\partial \xi^i}\frac{\partial \rho^\ell}{\partial \xi^j}, \qquad g^{ij} = \tilde g^{k\ell}\frac{\partial \xi^i}{\partial \rho^k}\frac{\partial \xi^j}{\partial \rho^\ell}. \tag{1.24}
$$

$g_{ij}$ lowers an index ($D_i = g_{ij}D^j$) and $g^{ij}$ raises one; the pair identifies $T_p$ with its dual.

### Length of a curve

For $\gamma : [a, b] \to S$ with $\dot\gamma^i = d(\xi^i \circ \gamma)/dt$,

$$
\lVert\gamma\rVert = \int_a^b\left\lVert\frac{d\gamma}{dt}\right\rVert dt = \int_a^b\sqrt{g_{ij}\dot\gamma^i\dot\gamma^j}\,dt. \tag{1.25}
$$

It does not depend on the parametrisation of $\gamma$ or on the coordinates.
In the infinitesimal form $ds^2 = g_{ij}d\xi^id\xi^j$ is the squared length of the displacement $d\xi$.

### Induced metric on a submanifold

If $M \subset S$ is a submanifold, $T_p(M) \subset T_p(S)$ and the restriction $g|_M$ is a Riemannian metric on $M$.
With coordinates $[u^a]$ on $M$ and $B^i_a = \partial \xi^i/\partial u^a$,

$$
g_{ab} = \left\langle\frac{\partial}{\partial u^a}, \frac{\partial}{\partial u^b}\right\rangle = g_{ij}B^i_aB^j_b. \tag{1.26}
$$

## Worked examples

### Polar coordinates and the sphere

From Cartesian $\delta_{ij}$, (1.22) gives the polar metric $\text{diag}(1, r^2)$ ([Vector Fields and Tensor Fields](03-Vector-Fields-and-Tensor-Fields.md)).
On the unit sphere in $\mathbb{R}^3$, (1.26) with the $B_\theta, B_\varphi$ of [Submanifolds](04-Submanifolds.md) gives $g = \text{diag}(1, \sin^2\theta)$, that is $ds^2 = d\theta^2 + \sin^2\theta\,d\varphi^2$.
The latitude $\theta = \pi/3$, parametrised by $\varphi \in [0, 2\pi]$, has length $2\pi\sin(\pi/3) = 5.4414$ by (1.25).

### The Fisher metric of the normal family

Section 2.2 shows the Fisher metric of $N(\mu, \sigma^2)$ in $(\mu, \sigma)$ coordinates is

$$
G = \begin{pmatrix} 1/\sigma^2 & 0 \\ 0 & 2/\sigma^2 \end{pmatrix}, \qquad ds^2 = \frac{d\mu^2 + 2\,d\sigma^2}{\sigma^2}.
$$

Lengths:

- From $N(0, 1)$ to $N(0, 4)$ along $\mu = 0$ (so $\sigma$ from 1 to 2): $\int_1^2\sqrt2/\sigma\,d\sigma = \sqrt2\ln2 = 0.9803$.
- Shifting the mean from 0 to 1 at fixed $\sigma = 1$ costs length 1; at $\sigma = 2$ the same shift costs only $0.5$.

"Moving the mean by a fixed amount is less distinguishable when the noise is larger, so the metric shrinks as $\sigma$ grows; this is a hyperbolic geometry, not a Euclidean one."

Changing to $(\mu, v = \sigma^2)$ with (1.22), $d\sigma/dv = 1/(2\sqrt v)$:

$$
\tilde g_{vv} = \frac{2}{\sigma^2}\left(\frac{1}{2\sqrt v}\right)^2 = \frac{1}{2v^2}, \qquad \tilde G = \text{diag}\left(\frac1v, \frac{1}{2v^2}\right),
$$

which at $v = 4$ is $\text{diag}(0.25, 0.03125)$.

## Pitfalls

- Assuming a manifold has a canonical metric; a parameter space is a manifold before it has a metric, and the Euclidean metric on parameters is generally not invariant under reparametrisation.
- Transforming $g^{ij}$ with the same Jacobians as $g_{ij}$; the inverse metric is contravariant.
- Computing the length of a curve in parameter space with the Euclidean formula; the result changes when the parameters change, while (1.25) does not.
- Forgetting the square root in (1.25); $\int g_{ij}\dot\gamma^i\dot\gamma^j\,dt$ is the energy, which depends on parametrisation.

## Review questions

> [!question]- ig-rm-definition | What is a Riemannian metric?
> A $C^\infty$ assignment of an inner product $\langle\,,\rangle_p$ (bilinear, symmetric, positive definite) to each tangent space $T_p(S)$; equivalently a smooth symmetric positive definite $(0, 2)$ tensor field.

> [!question]- ig-rm-transform | How does $[g_{ij}]$ transform under a change of coordinates, in matrix form?
> $\tilde G = J^\top GJ$ with $J = \partial \xi/\partial \rho$, that is $\tilde g_{k\ell} = g_{ij}(\partial \xi^i/\partial \rho^k)(\partial \xi^j/\partial \rho^\ell)$.

> [!question]- ig-rm-inverse | How does $g^{ij}$ transform, and why differently from $g_{ij}$?
> $\tilde g^{k\ell} = g^{ij}(\partial \rho^k/\partial \xi^i)(\partial \rho^\ell/\partial \xi^j)$, i.e. $\tilde G^{-1} = J^{-1}G^{-1}J^{-\top}$, the inverse of $J^\top GJ$. Upper indices transform contravariantly.

> [!question]- ig-rm-length | Write the length of a curve and say why it is well defined.
> $\lVert\gamma\rVert = \int_a^b\sqrt{g_{ij}\dot\gamma^i\dot\gamma^j}\,dt$. The integrand is the norm of the velocity, a coordinate-free quantity, and $\lVert\dot\gamma\rVert\,dt$ is invariant under reparametrisation.

> [!question]- ig-rm-induced | What metric does a submanifold inherit?
> $g_{ab} = g_{ij}B^i_aB^j_b$ with $B^i_a = \partial \xi^i/\partial u^a$ (equation 1.26), the restriction of $g$ to $T_p(M) \subset T_p(S)$.

> [!question]- ig-rm-normal-length | Under the Fisher metric $ds^2 = (d\mu^2 + 2d\sigma^2)/\sigma^2$, what is the length of the segment from $N(0, 1)$ to $N(0, 4)$ along $\mu = 0$?
> $\int_1^2\sqrt2/\sigma\,d\sigma = \sqrt2\ln2 \approx 0.9803$. (Section 1.10 shows this vertical line is a geodesic, so it is also the distance.)

> [!question]- ig-rm-mean-shift | Why does shifting the mean by 1 cost length 1 at $\sigma = 1$ but $0.5$ at $\sigma = 2$ under the Fisher metric?
> $g_{\mu\mu} = 1/\sigma^2$, so a horizontal segment of Euclidean length 1 has length $1/\sigma$. With more noise the two distributions are harder to tell apart.

> [!question]- ig-rm-v-coords | Rewrite $ds^2 = (d\mu^2 + 2d\sigma^2)/\sigma^2$ in $(\mu, v = \sigma^2)$.
> $ds^2 = d\mu^2/v + dv^2/(2v^2)$, since $d\sigma = dv/(2\sqrt v)$ and $2d\sigma^2/\sigma^2 = 2\,dv^2/(4v \cdot v)$.

## Where it leads

- [Riemannian Connection](10-Riemannian-Connection.md) builds the unique torsion-free connection compatible with $g$.
- [The Fisher Metric](../02-Geometric-Structure-of-Statistical-Models/02-The-Fisher-Metric.md) is the metric every statistical model carries.
- Code: [ch1_examples.py](code/ch1_examples.py).

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.5.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd edition, chapter 2 (metrics, lengths, induced metrics).
