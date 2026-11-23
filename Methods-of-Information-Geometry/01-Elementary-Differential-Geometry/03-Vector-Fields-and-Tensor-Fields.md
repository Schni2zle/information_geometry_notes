---
type: concept
tier: core
status: solid
section: 1.3
pages: 8-9
prereqs: [tangent-vectors-and-tangent-spaces]
est_hours: 2
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.3, Lee - Introduction to Smooth Manifolds 2nd ed ch 8 and 12]
---

# Vector Fields and Tensor Fields

## TL;DR

- A vector field $X$ assigns $X_p \in T_p(S)$ to each point; in coordinates $X = X^i\partial_i$ with component functions $X^i$, and it is $C^\infty$ when they are; $\mathcal{T}(S)$ is the set of smooth vector fields.
- Components transform contravariantly: $\tilde X^j = X^i\,\partial \rho^j/\partial \xi^i$ (1.13).
- A tensor field of type $(q, r)$, $q \in \{0, 1\}$, assigns a multilinear map $T_p \times \dots \times T_p \to \mathbb{R}$ (for $q = 0$) or $\to T_p$ (for $q = 1$) to each point.
- On fields, a tensor is $\mathcal{F}$-multilinear: $A(f_1X_1, \dots, f_rX_r) = f_1\cdots f_rA(X_1, \dots, X_r)$; conversely every $\mathcal{F}$-multilinear map comes from a pointwise tensor.
- Components $A_{i_1\dots i_r} = A(\partial_{i_1}, \dots, \partial_{i_r})$ pick up one Jacobian per lower index (1.15), and an extra inverse Jacobian for the upper index of a $(1, r)$ tensor (1.16).
- The book only needs types $(0, r)$ and $(1, r)$: metrics $(0, 2)$, cubic forms $(0, 3)$, curvature $(1, 3)$, torsion $(1, 2)$.

## Learning objectives

- Define vector fields, their components and the space $\mathcal{T}(S)$.
- Transform vector-field components between coordinate systems.
- Define tensor fields of type $(0, r)$ and $(1, r)$, their components and their transformation laws.
- Use $\mathcal{F}$-multilinearity to decide whether an operation on vector fields is a tensor.

## Core concepts

### Vector fields

A vector field is a map $X : p \mapsto X_p \in T_p(S)$.
The coordinate vector fields $\partial_i : p \mapsto (\partial/\partial \xi^i)_p$ form a basis at every point, so there are unique functions $X^i$ with $X_p = X^i(p)(\partial_i)_p$, written $X = X^i\partial_i$.
In another coordinate system $[\rho^j]$, $X = \tilde X^j\tilde\partial_j$ with

$$
\tilde X^j = X^i\frac{\partial \rho^j}{\partial \xi^i}, \qquad X^i = \tilde X^j\frac{\partial \xi^i}{\partial \rho^j}. \tag{1.13}
$$

If the components are $C^\infty$ in one coordinate system they are $C^\infty$ in all; the book calls such fields simply vector fields and writes $\mathcal{T}(S)$ or $\mathcal{T}$ for them.
$\mathcal{T}$ is a vector space under $(X + Y)_p = X_p + Y_p$ and $(cX)_p = cX_p$, and also an $\mathcal{F}$-module: $(fX)_p = f(p)X_p$.

### Multilinear maps and tensors at a point

$F : V_1 \times \dots \times V_r \to W$ is multilinear if it is linear in each argument with the others fixed.
At each $p$ let $[T_p]^0_r$ be the multilinear maps $T_p \times \dots \times T_p \to \mathbb{R}$ ($r$ factors) and $[T_p]^1_r$ those into $T_p$.
A tensor field of type $(q, r)$ is a map $p \mapsto A_p \in [T_p]^q_r$ for $q = 0$ or $1$: covariant degree $r$ and contravariant degree $q$.
A vector field is a tensor field of type $(1, 0)$.
Higher contravariant degrees exist but the book never uses them.

### Tensor fields as $\mathcal{F}$-multilinear maps

Given a tensor field $A$ and vector fields $X_1, \dots, X_r$, the map

$$
A(X_1, \dots, X_r) : p \mapsto A_p((X_1)_p, \dots, (X_r)_p) \tag{1.14}
$$

is a function (for $q = 0$) or a vector field (for $q = 1$), $C^\infty$ when $A$ is.
So $A$ defines a map $\mathcal{T} \times \dots \times \mathcal{T} \to \mathcal{F}$ or $\to \mathcal{T}$ which is $\mathcal{F}$-multilinear,

$$
A(f_1X_1, \dots, f_rX_r) = f_1\cdots f_rA(X_1, \dots, X_r), \qquad f_i \in \mathcal{F},
$$

and additive in each slot.
Conversely an $\mathcal{F}$-multilinear map $\mathcal{T}^r \to \mathcal{F}$ or $\to \mathcal{T}$ comes from a unique tensor field.
The practical test "is this a tensor?" is therefore: does it pull out functions, not only constants?

### Components and transformation laws

For a $(0, r)$ tensor the components with respect to $[\xi^i]$ are the $n^r$ functions $A_{i_1\dots i_r} = A(\partial_{i_1}, \dots, \partial_{i_r})$, and by $\mathcal{F}$-multilinearity

$$
A(X_1, \dots, X_r) = A_{i_1\dots i_r}X_1^{i_1}\cdots X_r^{i_r}.
$$

For a $(1, r)$ tensor, $A(\partial_{i_1}, \dots, \partial_{i_r}) = A^k_{i_1\dots i_r}\partial_k$ defines $n^{r+1}$ components and $A(X_1, \dots, X_r) = (A^k_{i_1\dots i_r}X_1^{i_1}\cdots X_r^{i_r})\partial_k$.
Changing to $[\rho^j]$, with tildes for the new components:

$$
\tilde A_{j_1\dots j_r} = A_{i_1\dots i_r}\frac{\partial \xi^{i_1}}{\partial \rho^{j_1}}\cdots\frac{\partial \xi^{i_r}}{\partial \rho^{j_r}}, \tag{1.15}
$$

$$
\tilde A^\ell_{j_1\dots j_r} = A^k_{i_1\dots i_r}\frac{\partial \xi^{i_1}}{\partial \rho^{j_1}}\cdots\frac{\partial \xi^{i_r}}{\partial \rho^{j_r}}\frac{\partial \rho^\ell}{\partial \xi^k}. \tag{1.16}
$$

Each lower index brings $\partial \xi/\partial \rho$ and each upper index brings $\partial \rho/\partial \xi$; this is exactly what makes $A(X_1, \dots, X_r)$ independent of coordinates.

## Worked examples

### The field $\partial_x$ in polar coordinates

By (1.13) the polar components of $\partial_x$ (components $(1, 0)$ in Cartesian) are $\partial r/\partial x = \cos\theta$ and $\partial\theta/\partial x = -\sin\theta/r$:

$$
\partial_x = \cos\theta\,\partial_r - \frac{\sin\theta}{r}\partial_\theta.
$$

At $(r, \theta) = (2, \pi/3)$ the components are $(0.5, -0.4330)$.
Two more to know: the rotation field $-y\partial_x + x\partial_y$ is $\partial_\theta$, and the Euler field $x\partial_x + y\partial_y$ is $r\partial_r$.

### Transforming a metric tensor

The Euclidean inner product is a $(0, 2)$ tensor with Cartesian components $\delta_{ij}$.
By (1.15), $\tilde g_{ab} = \delta_{ij}\frac{\partial \xi^i}{\partial \rho^a}\frac{\partial \xi^j}{\partial \rho^b} = (J^\top J)_{ab}$ with $J = \partial(x, y)/\partial(r, \theta)$, which gives $\text{diag}(1, r^2)$, the familiar $ds^2 = dr^2 + r^2d\theta^2$.

### The Lie bracket is not a tensor

The bracket $[X, Y]f = X(Yf) - Y(Xf)$ is $\mathbb{R}$-bilinear but not $\mathcal{F}$-bilinear.
Take $X = \partial_x$, $Y = \partial_y$ and $f = x$: $[\partial_x, x\partial_y] = \partial_y$, while $x[\partial_x, \partial_y] = 0$.
In general $[X, fY] = f[X, Y] + (Xf)Y$, and the extra term is what fails the test.
The same test shows later that $\nabla_XY$ is a tensor in $X$ but not in $Y$ ([Affine Connections](06-Affine-Connections-and-Covariant-Derivatives.md)).

## Pitfalls

- Treating component arrays as tensors; a list of $n^r$ functions is a tensor only if it transforms by (1.15) or (1.16), and connection coefficients are the standard counterexample.
- Checking only $\mathbb{R}$-linearity; a tensor must pull out arbitrary smooth functions.
- Mixing up which Jacobian goes with which index; lower (covariant) indices take $\partial \xi/\partial \rho$, upper (contravariant) ones take $\partial \rho/\partial \xi$.
- Assuming a non-zero vector field exists in every manifold; on the sphere every smooth field vanishes somewhere (hairy ball theorem), which is one reason global coordinates are special.

## Review questions

> [!question]- ig-tf-vector-field-transform | How do the components $X^i$ of a vector field transform under a change to $[\rho^j]$?
> $\tilde X^j = X^i\,\partial \rho^j/\partial \xi^i$ (equation 1.13), the inverse of the way the basis $\partial_i$ transforms.

> [!question]- ig-tf-type-definition | What is a tensor field of type $(q, r)$ with $q \in \{0, 1\}$?
> A smooth assignment to each $p$ of a multilinear map from $r$ copies of $T_p$ to $\mathbb{R}$ (if $q = 0$) or to $T_p$ (if $q = 1$). Covariant degree $r$, contravariant degree $q$.

> [!question]- ig-tf-f-multilinear | What is $\mathcal{F}$-multilinearity, and why does it matter?
> $A(f_1X_1, \dots, f_rX_r) = f_1\cdots f_rA(X_1, \dots, X_r)$ for smooth functions $f_i$, plus additivity. A map on vector fields comes from a pointwise tensor iff it is $\mathcal{F}$-multilinear, so this is the test for being a tensor.

> [!question]- ig-tf-component-law | Write the transformation law for the components of a $(0, 2)$ tensor and apply it to the Euclidean metric in polar coordinates.
> $\tilde g_{ab} = g_{ij}\,(\partial \xi^i/\partial \rho^a)(\partial \xi^j/\partial \rho^b)$. With $g = I$ and the polar Jacobian this gives $J^\top J = \text{diag}(1, r^2)$.

> [!question]- ig-tf-dx-polar | Express $\partial_x$ in polar coordinates.
> $\partial_x = \cos\theta\,\partial_r - (\sin\theta/r)\partial_\theta$, from $\tilde X^j = \partial \rho^j/\partial x$.

> [!question]- ig-tf-bracket-not-tensor | Show that the Lie bracket is not a tensor.
> $[X, fY] = f[X, Y] + (Xf)Y$. For example $[\partial_x, x\partial_y] = \partial_y \neq x[\partial_x, \partial_y] = 0$, so it is not $\mathcal{F}$-linear in its second slot.

> [!question]- ig-tf-examples-in-book | Name a tensor field of each type $(0, 2)$, $(0, 3)$, $(1, 2)$ and $(1, 3)$ that the book uses.
> $(0, 2)$: the Riemannian (Fisher) metric. $(0, 3)$: the skewness tensor $T_{ijk}$ of section 2.3. $(1, 2)$: the torsion of a connection, or the difference of two connections. $(1, 3)$: the Riemann-Christoffel curvature.

## Where it leads

- [Riemannian Metrics](05-Riemannian-Metrics.md) is a $(0, 2)$ tensor field.
- [Affine Connections](06-Affine-Connections-and-Covariant-Derivatives.md): the difference of two connections is a $(1, 2)$ tensor even though connection coefficients are not.
- Code: [ch1_examples.py](code/ch1_examples.py).

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.3.
- John M. Lee, *Introduction to Smooth Manifolds*, 2nd edition, chapters 8 (vector fields, Lie brackets) and 12 (tensors, the tensor characterisation lemma).
