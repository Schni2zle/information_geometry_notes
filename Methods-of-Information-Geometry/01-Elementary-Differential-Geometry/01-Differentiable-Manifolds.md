---
type: concept
tier: core
status: solid
section: 1.1
pages: 1-4
prereqs: []
est_hours: 2
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.1, Lee - Introduction to Smooth Manifolds 2nd ed ch 1, Tu - An Introduction to Manifolds 2nd ed ch 2 and 5]
---

# Differentiable Manifolds

## TL;DR

- A manifold $S$ is a set with coordinate systems $\varphi : S \to \mathbb{R}^n$, one-to-one onto an open set, such that any two are related by a $C^\infty$ diffeomorphism $\psi \circ \varphi^{-1}$.
- Doing geometry on a manifold means studying properties that are invariant under coordinate changes; that is why the coordinate changes must be smooth.
- Points of the manifolds in this book are probability distributions (chapters 2 to 4) or linear systems (chapter 5); $(\mu, \sigma)$ is a coordinate system on the set of normal distributions.
- A function $f : S \to \mathbb{R}$ is $C^\infty$ when $\bar f = f \circ \varphi^{-1}$ is; its partial derivatives $\partial f / \partial \xi^i$ are defined through $\bar f$.
- Jacobians of a coordinate change and its inverse are inverse matrices, $\frac{\partial \xi^i}{\partial \rho^j}\frac{\partial \rho^j}{\partial \xi^k} = \delta^i_k$, and the chain rule converts partial derivatives (1.2)-(1.3).
- Einstein convention: an index that appears once up and once down is summed.

## Learning objectives

- State the definition of an $n$-dimensional $C^\infty$ manifold $(S, \mathcal{A})$ in the book's form.
- Explain why the book only needs global coordinate systems, and give manifolds that do not have one.
- Define $C^\infty$ functions, their partial derivatives and the algebra $\mathcal{F}(S)$.
- Compute the Jacobian of a coordinate change and verify the identities (1.2)-(1.3).
- Read and write expressions in Einstein summation notation.
- Define smooth maps and diffeomorphisms between manifolds.

## Core concepts

### Sets with coordinates

Intuitively, a manifold is "a set with a coordinate system".
A coordinate system is a one-to-one map $\varphi : S \to \mathbb{R}^n$, $p \mapsto [\xi^1(p), \dots, \xi^n(p)]$, and $n = \dim S$.
The functions $\xi^i : S \to \mathbb{R}$ are the coordinate functions; the book writes $\xi^i$ both for the $i$-th coordinate of a point and for the function, like writing $y = y(x)$.

A coordinate system whose domain is all of $S$ is global.
The sphere and the torus have no global coordinate system; they are covered by overlapping open sets, each with its own local coordinates.
The book restricts itself to manifolds with a global coordinate system because information geometry mostly uses local properties, and every statistical model in the book comes with one (a parameter $\theta$ labels each distribution).

### Coordinate changes and the definition

If $\varphi = [\xi^i]$ and $\psi = [\rho^i]$ are two coordinate systems, the coordinate transformation is

$$
\psi \circ \varphi^{-1} : [\xi^1, \dots, \xi^n] \mapsto [\rho^1, \dots, \rho^n]. \tag{1.1}
$$

**Definition.** A set $S$ with a set $\mathcal{A}$ of coordinate systems is an $n$-dimensional $C^\infty$ differentiable manifold if

1. each $\varphi \in \mathcal{A}$ is one-to-one from $S$ onto an open subset of $\mathbb{R}^n$;
2. for every $\varphi \in \mathcal{A}$ and every one-to-one $\psi : S \to \mathbb{R}^n$: $\psi \in \mathcal{A}$ iff $\psi \circ \varphi^{-1}$ is a $C^\infty$ diffeomorphism.

Condition 2 makes $\mathcal{A}$ maximal: once one chart is fixed, every smoothly related chart is admitted.
The book reads $C^\infty$ as "sufficiently smooth"; finitely many derivatives would usually do.

Consequences:

- An open set $U \subset S$ is one whose image $\varphi(U)$ is open; by condition 2 this does not depend on $\varphi$, so $S$ is a topological space.
- An open subset $U$ with the restricted coordinates $\varphi|_U$ is again an $n$-dimensional manifold.

### Smooth functions and partial derivatives

A function $f : S \to \mathbb{R}$ is written in coordinates as $\bar f = f \circ \varphi^{-1}$, so $f(p) = \bar f(\xi^1, \dots, \xi^n)$.
The partial derivative of $f$ is defined by pulling back the ordinary one:

$$
\frac{\partial f}{\partial \xi^i} \overset{\text{def}}{=} \frac{\partial \bar f}{\partial \xi^i} \circ \varphi : S \to \mathbb{R},
$$

with value $(\partial f / \partial \xi^i)_p$ at $p$.
$f$ is $C^\infty$ when $\bar f$ is, and this does not depend on the coordinate system.
Mixed partials commute, $\frac{\partial^2 f}{\partial \xi^i \partial \xi^j} = \frac{\partial^2 f}{\partial \xi^j \partial \xi^i}$.
$\mathcal{F}(S)$ (or $\mathcal{F}$) is the set of $C^\infty$ functions; it is closed under pointwise sum, scalar multiple and product.

### Jacobians and the chain rule

For two coordinate systems $[\xi^i]$ and $[\rho^j]$, both Jacobian matrices exist and are inverse to each other:

$$
\sum_{j=1}^n \frac{\partial \xi^i}{\partial \rho^j}\frac{\partial \rho^j}{\partial \xi^k} = \sum_{j=1}^n \frac{\partial \rho^i}{\partial \xi^j}\frac{\partial \xi^j}{\partial \rho^k} = \delta^i_k. \tag{1.2}
$$

For $f \in \mathcal{F}$, the chain rule reads

$$
\frac{\partial f}{\partial \rho^j} = \sum_{i=1}^n \frac{\partial \xi^i}{\partial \rho^j}\frac{\partial f}{\partial \xi^i}, \qquad \frac{\partial f}{\partial \xi^i} = \sum_{j=1}^n \frac{\partial \rho^j}{\partial \xi^i}\frac{\partial f}{\partial \rho^j}. \tag{1.3}
$$

### Einstein's convention

An index that appears both as a superscript and as a subscript in one term is summed over $1, \dots, n$, so (1.2) is $\frac{\partial \xi^i}{\partial \rho^j}\frac{\partial \rho^j}{\partial \xi^k} = \delta^i_k$ and (1.3) is $\frac{\partial f}{\partial \rho^j} = \frac{\partial \xi^i}{\partial \rho^j}\frac{\partial f}{\partial \xi^i}$.
Similarly $A^i_j B^j_k$ means $\sum_j A^i_jB^j_k$, and $A^i_jX^j = A^i_kX^k$ because the name of a summed (dummy) index does not matter.
Coordinates carry upper indices ($\xi^i$) and derivatives $\partial/\partial \xi^i$ count as lower indices; this bookkeeping makes every valid formula balance its free indices.

### Maps between manifolds

A map $\lambda : S \to Q$ between manifolds with coordinates $\varphi$ and $\psi$ is $C^\infty$ when $\psi \circ \lambda \circ \varphi^{-1}$ is $C^\infty$ on the open set where it is defined.
Equivalently, $f \circ \lambda \in \mathcal{F}(S)$ for every $f \in \mathcal{F}(Q)$.
A $C^\infty$ bijection whose inverse is $C^\infty$ is a diffeomorphism; diffeomorphic manifolds are the same object as far as differential geometry is concerned.

## Worked examples

### Polar coordinates on the punctured plane

Let $S = \mathbb{R}^2 \setminus \{(x, 0) : x \ge 0\}$ with Cartesian $[\xi^i] = [x, y]$ and polar $[\rho^i] = [r, \theta]$, $\theta \in (0, 2\pi)$.
The Jacobian at $(r, \theta) = (2, \pi/3)$ is

$$
\frac{\partial(x, y)}{\partial(r, \theta)} = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix} = \begin{pmatrix} 0.5 & -1.7321 \\ 0.8660 & 1 \end{pmatrix},
$$

with determinant $r = 2$, and the inverse Jacobian is

$$
\frac{\partial(r, \theta)}{\partial(x, y)} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta/r & \cos\theta/r \end{pmatrix} = \begin{pmatrix} 0.5 & 0.8660 \\ -0.4330 & 0.25 \end{pmatrix}.
$$

Their product is the identity, which is (1.2).
"The slit is needed because polar coordinates are not one-to-one on the whole plane; removing a ray gives a global chart, which is the situation the book assumes."

### Three coordinate systems on the normal family

The normal distributions $N(\mu, \sigma^2)$ form a 2-dimensional manifold $S$ (the example in the book's preface).
Three useful coordinate systems are $(\mu, \sigma)$, $(\mu, v = \sigma^2)$ and the natural parameters $(\theta^1, \theta^2) = (\mu/\sigma^2, -1/(2\sigma^2))$ that reappear in section 2.3.
At $(\mu, \sigma) = (1, 2)$ the natural parameters are $(0.25, -0.125)$ and

$$
\frac{\partial(\theta^1, \theta^2)}{\partial(\mu, \sigma)} = \begin{pmatrix} 1/\sigma^2 & -2\mu/\sigma^3 \\ 0 & 1/\sigma^3 \end{pmatrix} = \begin{pmatrix} 0.25 & -0.25 \\ 0 & 0.125 \end{pmatrix},
$$

with determinant $1/\sigma^5 = 0.03125 \neq 0$.
The map is a diffeomorphism from $\{\sigma > 0\}$ onto the open set $\{\theta^2 < 0\}$, so the natural parameters are an admissible coordinate system in the sense of condition 2.

### A manifold without a global chart

"Why can't the sphere $S^2$ have a single coordinate system in the book's sense?"
A global chart would be a homeomorphism from the compact $S^2$ onto an open subset of $\mathbb{R}^2$, but a non-empty open subset of $\mathbb{R}^2$ is never compact.
Two stereographic projections, from the north and from the south pole, cover it, and they are related by $z \mapsto z/\lvert z\rvert^2$ on the overlap, which is smooth away from 0.

## Pitfalls

- Treating the coordinates as the manifold; geometric statements must be invariant under coordinate changes, and a quantity that changes when you reparametrise (like the raw Euclidean distance between parameter vectors) is not geometric.
- Forgetting that the image of a chart must be open; $(\mu, \sigma)$ with $\sigma \ge 0$ is not a valid coordinate domain, because $\sigma = 0$ is not a distribution with a density.
- Using a reparametrisation that is smooth but has a smooth inverse only away from some points (for example $\sigma \mapsto \sigma^3$ on $\mathbb{R}$, whose inverse is not differentiable at 0).
- Reading Einstein notation as summing over any repeated index; summation is only over one upper and one lower occurrence, and $g_{ii}$ in this book is not a trace unless written with an explicit sum.
- Confusing $\partial f/\partial \xi^1$ in two coordinate systems that share the coordinate $\xi^1$; a partial derivative depends on which other coordinates are held fixed.
  On $\mu > 0$, $\partial/\partial \mu$ in $(\mu, \sigma)$ holds $\sigma$ fixed, while in $(\mu, c)$ with $c = \sigma/\mu$ it holds $c$ fixed and so also moves $\sigma$: there it equals $\partial_\mu + c\,\partial_\sigma$.

## Review questions

> [!question]- ig-mfd-definition | State the book's definition of an $n$-dimensional $C^\infty$ manifold $(S, \mathcal{A})$.
> A set $S$ and a set $\mathcal{A}$ of one-to-one maps $\varphi : S \to \mathbb{R}^n$ such that each $\varphi$ maps onto an open set, and for every $\varphi \in \mathcal{A}$ a one-to-one $\psi$ belongs to $\mathcal{A}$ iff $\psi \circ \varphi^{-1}$ is a $C^\infty$ diffeomorphism.

> [!question]- ig-mfd-why-smooth-changes | Why does the definition require coordinate changes to be smooth?
> Geometry on a manifold studies properties invariant under coordinate changes, and differential operators must not depend on the choice of coordinates. Smooth changes with smooth inverses guarantee that smoothness and derivatives defined in one chart make sense in every other.

> [!question]- ig-mfd-global-chart | Give two manifolds without a global coordinate system, and say why the book can ignore them.
> The sphere and the torus (compact, so not homeomorphic to an open subset of $\mathbb{R}^n$). Information geometry mostly studies local properties, and statistical models come parametrised by $\theta$, which is a global coordinate system.

> [!question]- ig-mfd-partial-derivative | How is $\partial f/\partial \xi^i$ defined for $f : S \to \mathbb{R}$?
> Write $\bar f = f \circ \varphi^{-1}$ on $\varphi(S) \subset \mathbb{R}^n$ and set $\partial f/\partial \xi^i = (\partial \bar f/\partial \xi^i) \circ \varphi$. It is a function on $S$ again.

> [!question]- ig-mfd-jacobian-identity | What is $\frac{\partial \xi^i}{\partial \rho^j}\frac{\partial \rho^j}{\partial \xi^k}$, and why?
> $\delta^i_k$ (equation 1.2). It is the chain rule applied to $\xi^i = \xi^i(\rho(\xi))$: the Jacobians of a coordinate change and of its inverse are inverse matrices.

> [!question]- ig-mfd-einstein | Expand $A^i_jX^j$ and say which indices are free in $\frac{\partial \xi^i}{\partial \rho^j}\frac{\partial f}{\partial \xi^i}$.
> $A^i_jX^j = \sum_{j=1}^n A^i_jX^j$. In the second expression $i$ is summed (once up, once down) and $j$ is free, so it is a quantity with one lower index: $\partial f/\partial \rho^j$.

> [!question]- ig-mfd-natural-params | Show that $(\mu, \sigma) \mapsto (\mu/\sigma^2, -1/(2\sigma^2))$ is a valid coordinate change on the normal family.
> It is a smooth bijection from $\{\sigma > 0\}$ onto the open set $\{\theta^2 < 0\}$ with inverse $\sigma = (-2\theta^2)^{-1/2}$, $\mu = \theta^1\sigma^2$, also smooth. Its Jacobian determinant is $1/\sigma^5 \neq 0$.

> [!question]- ig-mfd-diffeomorphism | When is a map $\lambda : S \to Q$ a diffeomorphism?
> When it is a bijection, $C^\infty$ (that is, $f \circ \lambda \in \mathcal{F}(S)$ for all $f \in \mathcal{F}(Q)$, equivalently $\psi \circ \lambda \circ \varphi^{-1}$ is $C^\infty$), and its inverse is also $C^\infty$.

## Where it leads

- [Tangent Vectors and Tangent Spaces](02-Tangent-Vectors-and-Tangent-Spaces.md) builds the linear space attached to each point.
- [Statistical Models](../02-Geometric-Structure-of-Statistical-Models/01-Statistical-Models.md) makes a family $\{p_\xi\}$ a manifold with $\xi$ as coordinates.
- Code: [ch1_examples.py](code/ch1_examples.py) asserts the Jacobians above.

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.1.
- John M. Lee, *Introduction to Smooth Manifolds*, 2nd edition, chapter 1 (charts, atlases and smooth structures).
- Loring W. Tu, *An Introduction to Manifolds*, 2nd edition, chapters 2 and 5.
