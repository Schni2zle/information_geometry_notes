---
type: concept
tier: core
status: solid
section: 1.4
pages: 10-11
prereqs: [vector-fields-and-tensor-fields]
est_hours: 1.5
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.4, Lee - Introduction to Smooth Manifolds 2nd ed ch 5]
---

# Submanifolds

## TL;DR

- $M \subset S$ with coordinates $[u^a]$ is a submanifold if (i) each $\xi^i|_M$ is smooth, (ii) the vectors $B_a = [\partial \xi^i/\partial u^a]$ are linearly independent at every point, and (iii) the topology of $M$ is the one induced from $S$.
- Equivalently the embedding $\iota : M \to S$ is smooth, its differential is injective, and $M$ carries the subspace topology.
- Locally every submanifold is a coordinate slice $\{\xi^{m+1} = c^{m+1}, \dots, \xi^n = c^n\}$ of a suitable coordinate system.
- $T_p(M)$ is the $m$-dimensional subspace of $T_p(S)$ spanned by $\partial_a = B^i_a\partial_i$ (1.18).
- In statistics, a submodel of a statistical model is a submanifold: a curved exponential family is a curved submanifold of an exponential family.

## Learning objectives

- State conditions (i)-(iii) and explain what each rules out.
- Build a submanifold as a coordinate slice and recognise that every submanifold is locally one.
- Compute $B^i_a$ and identify $T_p(M)$ as a subspace of $T_p(S)$.
- Give examples and non-examples of submanifolds.

## Core concepts

### The definition

Let $M \subset S$ with $\dim S = n$, $\dim M = m$, coordinates $[\xi^i]$ on $S$ and $[u^a]$ on $M$.
Indices $i, j, k, \dots$ run over $1, \dots, n$ and $a, b, c, \dots$ over $1, \dots, m$.
$M$ is a submanifold of $S$ if:

1. the restriction $\xi^i|_M$ of each coordinate function is $C^\infty$ on $M$;
2. with $B^i_a = (\partial \xi^i/\partial u^a)_p$ and $B_a = [B^1_a, \dots, B^n_a] \in \mathbb{R}^n$, the vectors $B_1, \dots, B_m$ are linearly independent at every $p \in M$ (so $m \le n$);
3. for every open $W \subset M$ there is an open $U \subset S$ with $W = M \cap U$.

These conditions do not depend on the coordinate systems.
(i) and (ii) say that the embedding $\iota : M \to S$, $\iota(p) = p$, is smooth and has injective differential $(d\iota)_p$; (iii) says $M$ has the induced topology.
An open subset of $S$ is an $n$-dimensional submanifold.

### Coordinate slices

If $[\xi^i]$ is a coordinate system on $S$ and $c^{m+1}, \dots, c^n$ are constants, then

$$
M = \{p \in S \mid \xi^i(p) = c^i, \; m + 1 \le i \le n\},
$$

if non-empty, is an $m$-dimensional submanifold with coordinates $u^a = \xi^a|_M$.
Conversely, every $m$-dimensional submanifold is locally of this form: around each $p \in M$ there is an open $U \subset S$ and coordinates $[\xi^i]$ on $U$ with $M \cap U = \{\xi^i = c^i, m + 1 \le i \le n\}$ and $u^a = \xi^a$ on $M \cap U$.

### Tangent spaces of a submanifold

A curve $\gamma$ in $M$ is also a curve in $S$, so its velocity is in both $T_p(M)$ and $T_p(S)$.
With $\gamma^a = u^a \circ \gamma$ and $\gamma^i = \xi^i \circ \gamma$,

$$
\left(\frac{d\gamma^i}{dt}\right)_p = \left(\frac{\partial \xi^i}{\partial u^a}\right)_p\left(\frac{d\gamma^a}{dt}\right)_p. \tag{1.17}
$$

Condition (ii) makes this correspondence one-to-one; it is the differential $(d\iota)_p$, and through it $T_p(M)$ is a linear subspace of $T_p(S)$.
In particular,

$$
\left(\frac{\partial}{\partial u^a}\right)_p = \left(\frac{\partial \xi^i}{\partial u^a}\right)_p\left(\frac{\partial}{\partial \xi^i}\right)_p = B^i_a\,\partial_i, \tag{1.18}
$$

so $B_a$ is the coordinate representation of the basis vector $\partial_a$ of $M$ as a vector of $T_p(S)$.
As operators: $(\partial f/\partial u^a)_p = B^i_a(\partial f/\partial \xi^i)_p$ for all $f \in \mathcal{F}(S)$.

## Worked examples

### The sphere in $\mathbb{R}^3$

$M = S^2$ (minus the poles and a meridian, to have a global chart) with $u = (\theta, \varphi)$ and $\xi(u) = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$.
The columns of the Jacobian are

$$
B_\theta = (\cos\theta\cos\varphi, \cos\theta\sin\varphi, -\sin\theta), \qquad B_\varphi = (-\sin\theta\sin\varphi, \sin\theta\cos\varphi, 0).
$$

At $(\theta, \varphi) = (\pi/3, \pi/4)$: $B_\theta = (0.3536, 0.3536, -0.8660)$ and $B_\varphi = (-0.6124, 0.6124, 0)$, which have rank 2, so condition (ii) holds there.
$T_p(M)$ is the plane they span, orthogonal to the radius.

### A curved submodel of the normal family

The family $N(\mu, \mu^2)$, $\mu > 0$ (standard deviation proportional to the mean) is a 1-dimensional submanifold of the normal family.
In $(\mu, \sigma)$ coordinates it is the ray $\sigma = \mu$, a straight line.
In natural parameters $(\theta^1, \theta^2) = (\mu/\sigma^2, -1/(2\sigma^2)) = (1/\mu, -1/(2\mu^2))$, it is the parabola $\theta^2 = -(\theta^1)^2/2$.
"Whether a submanifold looks straight depends on the coordinates; section 1.8 replaces 'straight' by the coordinate-free notion 'autoparallel', and section 4.3 calls models like this curved exponential families."

### Two non-examples

- The cusp $\gamma(t) = (t^2, t^3)$: the velocity $(2t, 3t^2)$ vanishes at $t = 0$, so condition (ii) fails there.
- A figure-eight traced by an injective immersion of an open interval: (i) and (ii) hold, but near the crossing point small open arcs of the curve are not intersections of the curve with open sets of the plane, so (iii) fails.

## Pitfalls

- Thinking injectivity plus a non-vanishing velocity is enough; the figure-eight shows condition (iii) is needed.
- Confusing $\partial/\partial u^a$ of $M$ with $\partial/\partial \xi^a$ of $S$; they agree only for a coordinate slice with $u^a = \xi^a$.
- Assuming a submanifold has a natural connection; it inherits one only by projection (section 1.9) or when it is autoparallel (section 1.8).
- Forgetting that $m \le n$ follows from (ii): $m$ independent vectors in $\mathbb{R}^n$.

## Review questions

> [!question]- ig-sub-conditions | State the three conditions for $M \subset S$ to be a submanifold.
> (i) Each $\xi^i|_M$ is $C^\infty$ on $M$. (ii) $B_a = [\partial \xi^i/\partial u^a]$, $a = 1, \dots, m$, are linearly independent at each point. (iii) Every open set of $M$ is $M \cap U$ for some open $U \subset S$.

> [!question]- ig-sub-embedding | Restate conditions (i)-(iii) in terms of the embedding $\iota : M \to S$.
> $\iota$ is $C^\infty$, its differential $(d\iota)_p$ is injective at every point, and $M$ carries the topology induced from $S$.

> [!question]- ig-sub-tangent | How is $T_p(M)$ a subspace of $T_p(S)$?
> Through $(d\iota)_p$: $\partial/\partial u^a = B^i_a\,\partial/\partial \xi^i$ (equation 1.18), and the $B_a$ are independent, so $T_p(M)$ is the $m$-dimensional span of $B^i_a\partial_i$.

> [!question]- ig-sub-slice | What is the local normal form of an $m$-dimensional submanifold?
> Near each point there are coordinates $[\xi^i]$ of $S$ in which $M = \{\xi^{m+1} = c^{m+1}, \dots, \xi^n = c^n\}$ and $u^a = \xi^a$.

> [!question]- ig-sub-cusp | Is $\{(t^2, t^3)\}$ a submanifold of $\mathbb{R}^2$ with coordinate $t$?
> No: the velocity $(2t, 3t^2)$ is zero at $t = 0$, so condition (ii) fails (the image has a cusp at the origin).

> [!question]- ig-sub-curved-normal | What does $N(\mu, \mu^2)$ look like in $(\mu, \sigma)$ and in natural parameters?
> The ray $\sigma = \mu$ in $(\mu, \sigma)$, and the parabola $\theta^2 = -(\theta^1)^2/2$ in $(\theta^1, \theta^2) = (\mu/\sigma^2, -1/(2\sigma^2))$. Straightness is coordinate-dependent.

## Where it leads

- [Autoparallel Submanifolds](08-Autoparallel-Submanifolds.md) and [Projection of Connections and Embedding Curvature](09-Projection-of-Connections-and-Embedding-Curvature.md) study how a submanifold sits in $S$.
- [Riemannian Metrics](05-Riemannian-Metrics.md): a submanifold inherits a metric $g_{ab} = g_{ij}B^i_aB^j_b$.
- [Alpha-Affine Manifolds and Alpha-Families](../02-Geometric-Structure-of-Statistical-Models/06-Alpha-Affine-Manifolds-and-Alpha-Families.md): exponential and mixture families are autoparallel submanifolds of $\mathcal{P}(\mathcal{X})$.
- Code: [ch1_examples.py](code/ch1_examples.py).

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.4.
- John M. Lee, *Introduction to Smooth Manifolds*, 2nd edition, chapter 5 (embedded submanifolds, slice charts).
