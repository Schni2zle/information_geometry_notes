---
type: concept
tier: core
status: solid
section: 1.7
pages: 17-19
prereqs: [affine-connections-and-covariant-derivatives]
est_hours: 3
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.7, Lee - Introduction to Riemannian Manifolds 2nd ed ch 7, Kobayashi and Nomizu - Foundations of Differential Geometry vol 1 ch 3]
---

# Flatness

## TL;DR

- A vector field is parallel if $\nabla_YX = 0$ for all $Y$, i.e. $\partial_iX^k + X^j\Gamma^k_{ij} = 0$ (1.40); non-zero parallel fields do not exist in general.
- $[\xi^i]$ is an affine coordinate system for $\nabla$ if all $\partial_i$ are parallel, equivalently $\Gamma^k_{ij} \equiv 0$; $\nabla$ (or $S$) is flat if one exists.
- Affine coordinates are unique up to affine transformations $\xi = A\rho + B$ with $A$ regular (1.41).
- Curvature $R(X, Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$ and torsion $T(X, Y) = \nabla_XY - \nabla_YX - [X, Y]$ are tensors of types $(1, 3)$ and $(1, 2)$, with components (1.45)-(1.46).
- $\nabla$ is flat iff $R = 0$ and $T = 0$ (locally); a torsion-free connection ($\Gamma^k_{ij} = \Gamma^k_{ji}$) is called symmetric, and the book's connections are almost all symmetric.
- If $R = 0$ on a simply connected $S$, parallel translation is path-independent; if moreover $T \neq 0$ there are still no affine coordinates (distant parallelism).

## Learning objectives

- Define parallel vector fields, affine coordinate systems and flatness.
- Show that affine coordinate systems are related by affine transformations.
- Compute the curvature and torsion tensors from connection coefficients.
- State the flatness criterion and the relation between curvature and path-dependence of parallel translation.
- Explain why every 1-dimensional manifold is flat.

## Core concepts

### Parallel fields and affine coordinates

$X \in \mathcal{T}(S)$ is parallel on $S$ if it is parallel along every curve: $X_q = \Pi_\gamma(X_p)$ for any $\gamma$ from $p$ to $q$.
Equivalently $\nabla_YX = 0$ for all $Y$, or for $X = X^i\partial_i$,

$$
\partial_iX^k + X^j\Gamma^k_{ij} = 0. \tag{1.40}
$$

This is an overdetermined system, and in general it has no non-zero solution.

If all $n$ basis fields $\partial_i$ of $[\xi^i]$ are parallel, $[\xi^i]$ is an affine coordinate system for $\nabla$.
By (1.39) this is the same as $\nabla_{\partial_i}\partial_j = 0$, i.e. $\Gamma^k_{ij} \equiv 0$.
If an affine coordinate system exists, $\nabla$ is flat, or $S$ is flat with respect to $\nabla$.

### Affine coordinates are unique up to affine maps

If $[\xi^i]$ is affine, (1.29) gives the coefficients in $[\rho^r]$ as $\tilde\Gamma^t_{rs} = \frac{\partial^2\xi^k}{\partial \rho^r\partial \rho^s}\frac{\partial \rho^t}{\partial \xi^k}$.
So $[\rho^r]$ is also affine iff $\partial^2\xi^k/\partial \rho^r\partial \rho^s = 0$, i.e. there is a regular $n \times n$ matrix $A$ and $B \in \mathbb{R}^n$ with

$$
\xi(p) = A\rho(p) + B \qquad (\forall p \in S). \tag{1.41}
$$

This is an affine transformation (a linear transformation if $B = 0$); they form a group, and affine coordinates have exactly this freedom.

### Curvature and torsion

With the Lie bracket $[X, Y] = (X^j\partial_jY^i - Y^j\partial_jX^i)\partial_i$, a vector field independent of coordinates, define

$$
R(X, Y)Z = \nabla_X(\nabla_YZ) - \nabla_Y(\nabla_XZ) - \nabla_{[X,Y]}Z, \tag{1.42}
$$

$$
T(X, Y) = \nabla_XY - \nabla_YX - [X, Y]. \tag{1.43}
$$

Both are $\mathcal{F}$-multilinear, hence tensor fields of types $(1, 3)$ and $(1, 2)$: the Riemann-Christoffel curvature tensor and the torsion tensor of $\nabla$.
Their components, $R(\partial_i, \partial_j)\partial_k = R^\ell_{ijk}\partial_\ell$ and $T(\partial_i, \partial_j) = T^k_{ij}\partial_k$ (1.44), are

$$
R^\ell_{ijk} = \partial_i\Gamma^\ell_{jk} - \partial_j\Gamma^\ell_{ik} + \Gamma^h_{jk}\Gamma^\ell_{ih} - \Gamma^h_{ik}\Gamma^\ell_{jh}, \tag{1.45}
$$

$$
T^k_{ij} = \Gamma^k_{ij} - \Gamma^k_{ji}. \tag{1.46}
$$

In general $R^\ell_{ijk} = -R^\ell_{jik}$ and $T^k_{ij} = -T^k_{ji}$.

### The flatness criterion

If $[\xi^i]$ is affine, $R^\ell_{ijk} = 0$ and $T^k_{ij} = 0$ in that chart, and since they are tensors, they vanish in every chart.
So a flat connection has $R = 0$ and $T = 0$.
Conversely, if $R = 0$ and $T = 0$, $\nabla$ is locally flat: every point has a neighbourhood on which an affine coordinate system exists (proved in standard differential geometry texts).

A connection with $T = 0$, i.e. $\Gamma^k_{ij} = \Gamma^k_{ji}$, is symmetric or torsion-free.
The connections in information geometry are mostly symmetric; torsion may matter for quantum (non-commutative) probability and systems theory, and section 7.3 gives an example.

### Curvature and path-dependence

If $\nabla$ is flat, parallel translation does not depend on the curve: in affine coordinates $\Pi_\gamma((\partial_i)_p) = (\partial_i)_q$ for every $\gamma$, and $X = X^i\partial_i$ is parallel iff the $X^i$ are constants.
In general, path-independence of parallel translation is equivalent to the existence of $n$ independent parallel fields, which forces $R = 0$; on a simply connected $S$ the converse also holds.
When $R = 0$ but $T \neq 0$, parallel translation is path-independent yet there is no affine coordinate system; these spaces of distant parallelism (teleparallelism) were introduced by Einstein in unified field theory and also appear in non-Riemannian plasticity.

On a 1-dimensional manifold $R^1_{111}$ and $T^1_{11}$ vanish by antisymmetry, so every connection is flat.

## Worked examples

### A flat connection with non-zero coefficients

The polar coefficients of the Euclidean connection ($\Gamma^r_{\theta\theta} = -r$, $\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = 1/r$) are not zero, but plugging them into (1.45) gives $R^\ell_{ijk} = 0$ for every index, and they are symmetric, so $T = 0$.
The criterion recovers that the plane is flat even though polar coordinates are not affine.
For instance $R^r_{r\theta\theta} = \partial_r\Gamma^r_{\theta\theta} - \partial_\theta\Gamma^r_{r\theta} + \Gamma^h_{\theta\theta}\Gamma^r_{rh} - \Gamma^h_{r\theta}\Gamma^r_{\theta h} = -1 - 0 + 0 - \Gamma^\theta_{r\theta}\Gamma^r_{\theta\theta} = -1 + 1 = 0$.

### Curvature without torsion: the sphere

With the Riemannian connection of the unit sphere ([Riemannian Connection](10-Riemannian-Connection.md)), $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$ and $\Gamma^\varphi_{\theta\varphi} = \cot\theta$.
(1.45) gives $R^\theta_{\varphi\theta\varphi} = -\sin^2\theta \neq 0$, and the Gaussian curvature $\langle R(\partial_\theta, \partial_\varphi)\partial_\varphi, \partial_\theta\rangle/\det g$ equals 1.
So the sphere has no affine coordinates for this connection, and parallel translation is path-dependent (the holonomy example in section 1.10).

### Torsion without curvature: distant parallelism

On $\mathbb{R}^2$ take Cartesian coefficients $\Gamma^1_{12} = 1$, all others 0.
Then $T^1_{12} = \Gamma^1_{12} - \Gamma^1_{21} = 1$, and (1.45) gives $R = 0$ (the only candidate quadratic terms need two non-zero coefficients chained through the index $h$, and none chain).
The parallel fields solving (1.40) are $X = (d - cx)\partial_1 + c\,\partial_2$; two independent ones are $\partial_1$ and $-x\partial_1 + \partial_2$.
Their bracket is $[\partial_1, -x\partial_1 + \partial_2] = -\partial_1 \neq 0$, so they are not the coordinate fields of any chart: parallelism is path-independent but no affine coordinate system exists.

### An affine change of coordinates

$\rho \mapsto \xi = (2\rho^1 + \rho^2 + 1, \rho^1 - \rho^2)$ has $A = \begin{pmatrix} 2 & 1 \\ 1 & -1\end{pmatrix}$ with $\det A = -3 \neq 0$, so it maps affine coordinates to affine coordinates.
Polar coordinates fail (1.41) because $\partial^2x/\partial \theta^2 = -r\cos\theta \neq 0$.

## Pitfalls

- Judging flatness by whether $\Gamma$ vanishes in the coordinates you happen to use; flatness is about the existence of some chart with $\Gamma = 0$, which the tensors $R$ and $T$ detect.
- Forgetting torsion; $R = 0$ alone gives path-independent parallelism, not affine coordinates.
- Confusing "flat" for a connection with "flat" for a metric; section 2.5 shows the probability simplex is flat for the $e$- and $m$-connections but curved (part of a sphere) for the Levi-Civita connection of the Fisher metric.
- Mixing curvature sign or index conventions across books; the book uses $R(\partial_i, \partial_j)\partial_k = R^\ell_{ijk}\partial_\ell$ with (1.45), and some authors order indices differently.
- Assuming flat implies globally path-independent on any domain; a flat connection on a non-simply-connected space can still have holonomy around holes.

## Review questions

> [!question]- ig-flat-affine-coords | What is an affine coordinate system for $\nabla$, and when is $\nabla$ flat?
> Coordinates $[\xi^i]$ whose basis fields $\partial_i$ are all parallel, equivalently $\Gamma^k_{ij} \equiv 0$. $\nabla$ is flat if such coordinates exist.

> [!question]- ig-flat-affine-freedom | How are two affine coordinate systems of the same flat connection related?
> By an affine transformation $\xi = A\rho + B$ with $A$ regular (equation 1.41), because (1.29) with both $\Gamma$ zero forces $\partial^2\xi^k/\partial \rho^r\partial \rho^s = 0$.

> [!question]- ig-flat-curvature-components | Write the curvature components $R^\ell_{ijk}$ in terms of $\Gamma$.
> $R^\ell_{ijk} = \partial_i\Gamma^\ell_{jk} - \partial_j\Gamma^\ell_{ik} + \Gamma^h_{jk}\Gamma^\ell_{ih} - \Gamma^h_{ik}\Gamma^\ell_{jh}$, from $R(\partial_i, \partial_j)\partial_k = \nabla_i\nabla_j\partial_k - \nabla_j\nabla_i\partial_k$.

> [!question]- ig-flat-torsion | What is torsion, and when is a connection symmetric?
> $T(X, Y) = \nabla_XY - \nabla_YX - [X, Y]$, with $T^k_{ij} = \Gamma^k_{ij} - \Gamma^k_{ji}$. The connection is symmetric (torsion-free) iff $\Gamma^k_{ij} = \Gamma^k_{ji}$ in any (hence every) coordinate system.

> [!question]- ig-flat-criterion | State the criterion for flatness.
> $\nabla$ is (locally) flat iff $R = 0$ and $T = 0$. Necessity: both tensors vanish in affine coordinates, hence everywhere. Sufficiency is a standard theorem.

> [!question]- ig-flat-polar | Polar coordinates give $\Gamma^r_{\theta\theta} = -r \neq 0$. Is the plane curved?
> No. $\Gamma$ is not a tensor; computing $R$ from (1.45) gives 0 and the coefficients are symmetric, so the connection is flat, as Cartesian coordinates show directly.

> [!question]- ig-flat-teleparallel | Give a connection on $\mathbb{R}^2$ with $R = 0$ but $T \neq 0$, and say what fails.
> Cartesian $\Gamma^1_{12} = 1$, others 0. $T^1_{12} = 1$, $R = 0$. Parallel transport is path-independent, with parallel fields $\partial_1$ and $-x\partial_1 + \partial_2$, but their bracket is $-\partial_1 \neq 0$, so they are not coordinate fields and no affine chart exists.

> [!question]- ig-flat-one-dim | Why is every connection on a 1-dimensional manifold flat?
> $R^1_{111} = -R^1_{111}$ and $T^1_{11} = -T^1_{11}$ by antisymmetry, so both vanish. Concretely, an affine parameter exists along any curve (section 1.8).

> [!question]- ig-flat-sphere-curvature | What is the Gaussian curvature of the unit sphere, and what does it imply for parallel translation?
> 1 (from $R^\theta_{\varphi\theta\varphi} = -\sin^2\theta$ and $\det g = \sin^2\theta$). $R \neq 0$, so parallel translation is path-dependent and there are no affine coordinates.

## Where it leads

- [Autoparallel Submanifolds](08-Autoparallel-Submanifolds.md): in a flat space, autoparallel submanifolds are affine subspaces (Theorem 1.1).
- [Alpha-Affine Manifolds and Alpha-Families](../02-Geometric-Structure-of-Statistical-Models/06-Alpha-Affine-Manifolds-and-Alpha-Families.md): exponential and mixture families are flat for $\nabla^{(1)}$ and $\nabla^{(-1)}$, with natural and expectation parameters as affine coordinates.
- Code: [ch1_examples.py](code/ch1_examples.py) computes all curvature and torsion tensors quoted here.

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.7.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd edition, chapter 7 (curvature, flat manifolds).
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, volume 1, chapter 3 (torsion and curvature of linear connections).
