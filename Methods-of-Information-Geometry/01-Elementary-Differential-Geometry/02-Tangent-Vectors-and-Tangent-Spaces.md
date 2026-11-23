---
type: concept
tier: core
status: solid
section: 1.2
pages: 5-7
prereqs: [differentiable-manifolds]
est_hours: 2
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 1.2, Lee - Introduction to Smooth Manifolds 2nd ed ch 3]
---

# Tangent Vectors and Tangent Spaces

## TL;DR

- On an abstract manifold $\gamma'(a) = \lim(\gamma(a + h) - \gamma(a))/h$ makes no sense, so a tangent vector is defined as the directional-derivative operator $f \mapsto \frac{d}{dt}f(\gamma(t))\big|_{t=a}$.
- In coordinates $\left(\frac{d\gamma}{dt}\right)_p = \dot\gamma^i(a)\left(\frac{\partial}{\partial \xi^i}\right)_p$ (1.6): the coordinate partials $(\partial_i)_p$ are the tangent vectors of the coordinate curves.
- $T_p(S) = \{c^i(\partial_i)_p\}$ is an $n$-dimensional vector space with natural basis $\{(\partial_i)_p\}$ (1.8).
- Components change with the Jacobian: $(\partial/\partial \rho^j)_p = (\partial \xi^i/\partial \rho^j)_p(\partial/\partial \xi^i)_p$ (1.7).
- Tangent vectors are exactly the linear operators on $\mathcal{F}$ that obey Leibniz's rule (1.9)-(1.10).
- A smooth map $\lambda : S \to Q$ pushes tangent vectors forward by its differential $(d\lambda)_p : T_p(S) \to T_{\lambda(p)}(Q)$, the Jacobian matrix in coordinates (1.11)-(1.12).

## Learning objectives

- Define curves and tangent vectors of curves on a manifold without an ambient space.
- Express a tangent vector in a coordinate basis and change basis with the Jacobian.
- Explain why $\dim T_p(S) = \dim S$.
- State the derivation characterisation of tangent vectors.
- Compute the differential of a smooth map between manifolds and use it on tangent vectors of curves.

## Core concepts

### The idea: local linearisation

The tangent space $T_p$ at $p$ is the vector space obtained by "locally linearising" $S$ around $p$.
With coordinates $[\xi^i]$, let $e_i$ be the tangent vector through $p$ parallel to the $i$-th coordinate curve (vary only $\xi^i$); $T_p$ is spanned by $e_1, \dots, e_n$ (Figure 1.3).
If $p'$ is infinitesimally close to $p$ with coordinates $\xi^i + d\xi^i$, the segment $\overrightarrow{pp'}$ is the infinitesimal vector $d\xi^ie_i$.
The rest of the section makes this precise without infinitesimals.

### Curves and their tangent vectors

A curve is a one-to-one map $\gamma : I \to S$ from an interval; in coordinates $\gamma^i(t) = \xi^i(\gamma(t))$, and $\gamma$ is $C^\infty$ when each $\gamma^i$ is.
If $S$ sits inside some $\mathbb{R}^\ell$, the tangent vector is the ordinary derivative

$$
\dot\gamma(a) = \lim_{h \to 0}\frac{\gamma(a + h) - \gamma(a)}{h}, \tag{1.4}
$$

but on an abstract manifold the difference $\gamma(a + h) - \gamma(a)$ means nothing.
What does make sense is the rate of change of a function along the curve:

$$
\frac{d}{dt}f(\gamma(t)) = \left(\frac{\partial f}{\partial \xi^i}\right)_{\gamma(t)}\frac{d\gamma^i(t)}{dt}. \tag{1.5}
$$

So the tangent vector of $\gamma$ at $p = \gamma(a)$ is defined to be the operator $\left(\frac{d\gamma}{dt}\right)_p : \mathcal{F} \to \mathbb{R}$, $f \mapsto \frac{d}{dt}f(\gamma(t))\big|_{t=a}$, and (1.5) becomes

$$
\left(\frac{d\gamma}{dt}\right)_p = \dot\gamma^i(a)\left(\frac{\partial}{\partial \xi^i}\right)_p, \tag{1.6}
$$

where $(\partial/\partial \xi^i)_p : f \mapsto (\partial f/\partial \xi^i)_p$.
When $S$ is embedded in $\mathbb{R}^\ell$, this operator and the vector (1.4) correspond one-to-one, so the operator definition generalises the familiar one.
The operator $(\partial/\partial \xi^i)_p$ is the tangent vector of the $i$-th coordinate curve; it is the $e_i$ above.

### The tangent space

The set of tangent vectors of all curves through $p$ is

$$
T_p(S) = \left\{c^i\left(\frac{\partial}{\partial \xi^i}\right)_p \;\middle|\; [c^1, \dots, c^n] \in \mathbb{R}^n\right\}. \tag{1.8}
$$

The operators $(\partial/\partial \xi^i)_p$ are linearly independent, so $T_p(S)$ is a linear space of dimension $n = \dim S$; $\{(\partial_i)_p\}$ is the natural basis of the coordinate system $[\xi^i]$.
Changing to coordinates $[\rho^j]$ uses (1.3):

$$
\left(\frac{\partial}{\partial \rho^j}\right)_p = \left(\frac{\partial \xi^i}{\partial \rho^j}\right)_p\left(\frac{\partial}{\partial \xi^i}\right)_p, \qquad \left(\frac{\partial}{\partial \xi^i}\right)_p = \left(\frac{\partial \rho^j}{\partial \xi^i}\right)_p\left(\frac{\partial}{\partial \rho^j}\right)_p. \tag{1.7}
$$

### Tangent vectors as derivations

Every $D \in T_p$ satisfies, for $f, g \in \mathcal{F}$ and $a, b \in \mathbb{R}$,

$$
D(af + bg) = aD(f) + bD(g) \quad \text{(linearity)}, \tag{1.9}
$$

$$
D(f \cdot g) = f(p)D(g) + g(p)D(f) \quad \text{(Leibniz)}. \tag{1.10}
$$

Conversely, any operator $D : \mathcal{F} \to \mathbb{R}$ with these two properties is an element of $T_p$.
This gives a coordinate-free definition of the tangent space.

### The differential of a map

Let $\lambda : S \to Q$ be smooth.
For $D \in T_p(S)$ define $D' : \mathcal{F}(Q) \to \mathbb{R}$ by $D'(f) = D(f \circ \lambda)$; it satisfies (1.9)-(1.10) at $\lambda(p)$, so $D' \in T_{\lambda(p)}(Q)$.
The linear map $(d\lambda)_p : D \mapsto D'$ is the differential of $\lambda$ at $p$.
With coordinates $[\xi^i]$ on $S$ and $[\rho^j]$ on $Q$,

$$
(d\lambda)_p\left(\left(\frac{\partial}{\partial \xi^i}\right)_p\right) = \left(\frac{\partial(\rho^j \circ \lambda)}{\partial \xi^i}\right)_p\left(\frac{\partial}{\partial \rho^j}\right)_{\lambda(p)}, \tag{1.11}
$$

so its matrix is the Jacobian, and for a curve $\gamma$ through $p$,

$$
(d\lambda)_p\left(\left(\frac{d\gamma}{dt}\right)_p\right) = \left(\frac{d(\lambda \circ \gamma)}{dt}\right)_{\lambda(p)}. \tag{1.12}
$$

The differential sends the velocity of a curve to the velocity of its image.

## Worked examples

### One tangent vector, two coordinate systems

Take the parabola $\gamma(t) = (t, t^2)$ in the plane at $t = 1$, $p = (1, 1)$.
In Cartesian coordinates its components are $(\dot x, \dot y) = (1, 2)$.
In polar coordinates $r = \sqrt{x^2 + y^2}$ and $\theta = \arctan(y/x)$, so

$$
\dot r = \frac{x\dot x + y\dot y}{r} = \frac{3}{\sqrt2} = 2.1213, \qquad \dot\theta = \frac{x\dot y - y\dot x}{r^2} = \frac{1}{2},
$$

which is what (1.7) gives with the inverse polar Jacobian at $(r, \theta) = (\sqrt2, \pi/4)$.
The vector is the same object: applied to $f = x^2 + y^2 = r^2$ it gives $2x\dot x + 2y\dot y = 6$ in Cartesian and $2r\dot r = 2\sqrt2 \cdot 3/\sqrt2 = 6$ in polar.

### Differential of a reparametrisation of the normal family

Let $\lambda$ map $(\mu, \sigma)$ to the natural parameters $(\theta^1, \theta^2) = (\mu/\sigma^2, -1/(2\sigma^2))$ (an identity map of the manifold written between two charts).
At $(\mu, \sigma) = (1, 2)$, (1.11) gives

$$
(d\lambda)_p(\partial_\sigma) = \frac{\partial \theta^1}{\partial \sigma}\partial_{\theta^1} + \frac{\partial \theta^2}{\partial \sigma}\partial_{\theta^2} = -0.25\,\partial_{\theta^1} + 0.125\,\partial_{\theta^2}.
$$

"Increasing the standard deviation at fixed mean lowers $\theta^1$ and raises $\theta^2$ towards 0; in natural coordinates the direction 'more spread' is not a coordinate axis."

### A derivation that is not a tangent vector

"Is $D(f) = f(p)$ a tangent vector?"
It is linear, but $D(fg) = f(p)g(p)$ while Leibniz requires $f(p)g(p) + g(p)f(p) = 2f(p)g(p)$, so no.
Every tangent vector kills constants: $D(1) = D(1 \cdot 1) = 2D(1)$, so $D(1) = 0$; the evaluation map gives $D(1) = 1$.

## Pitfalls

- Picturing $T_p(S)$ as a subset of $S$; it is a separate vector space attached at $p$, and $T_p$ and $T_q$ for $p \neq q$ have no natural identification until a connection is chosen (section 1.6).
- Transforming basis vectors and components the same way; the basis $\partial_i$ transforms with $\partial \xi^i/\partial \rho^j$ while components $c^i$ transform with the inverse matrix $\partial \rho^j/\partial \xi^i$, which keeps $c^i\partial_i$ unchanged.
- Thinking the velocity depends only on the image of the curve; reparametrising $t \mapsto 2t$ doubles it.
- Forgetting that $\partial/\partial \xi^1$ depends on the whole coordinate system, not only on $\xi^1$ (see the pitfall in [Differentiable Manifolds](01-Differentiable-Manifolds.md)).

## Review questions

> [!question]- ig-tan-why-operator | Why does the book define a tangent vector as an operator on functions rather than as $\lim(\gamma(a + h) - \gamma(a))/h$?
> On an abstract manifold points cannot be subtracted, so the limit is undefined. The rate of change $\frac{d}{dt}f(\gamma(t))$ of a function along the curve is always defined, and it determines the velocity.

> [!question]- ig-tan-coordinate-form | Write the tangent vector of $\gamma$ at $p = \gamma(a)$ in the natural basis.
> $\left(\frac{d\gamma}{dt}\right)_p = \dot\gamma^i(a)\left(\frac{\partial}{\partial \xi^i}\right)_p$ with $\gamma^i = \xi^i \circ \gamma$ (equation 1.6).

> [!question]- ig-tan-dimension | Why is $\dim T_p(S) = n$?
> $T_p(S) = \{c^i(\partial_i)_p\}$ and the $n$ operators $(\partial_i)_p$ are linearly independent: applied to the coordinate function $\xi^k$ they give $\delta^k_i$.

> [!question]- ig-tan-basis-change | How do the natural basis vectors and the components of a tangent vector transform from $[\xi^i]$ to $[\rho^j]$?
> Basis: $\partial/\partial \rho^j = (\partial \xi^i/\partial \rho^j)\partial/\partial \xi^i$. Components: $\tilde c^j = (\partial \rho^j/\partial \xi^i)c^i$. The two Jacobians are inverse, so $c^i\partial_i$ is unchanged.

> [!question]- ig-tan-derivation | Which two properties characterise tangent vectors at $p$ as operators on $\mathcal{F}$?
> Linearity $D(af + bg) = aD(f) + bD(g)$ and Leibniz's rule $D(fg) = f(p)D(g) + g(p)D(f)$. Every such operator is $c^i(\partial_i)_p$ for some $c$.

> [!question]- ig-tan-kills-constants | Show that any tangent vector annihilates constant functions.
> $D(1) = D(1 \cdot 1) = 1 \cdot D(1) + 1 \cdot D(1) = 2D(1)$, so $D(1) = 0$; by linearity $D(c) = 0$ for every constant.

> [!question]- ig-tan-differential | Define the differential $(d\lambda)_p$ of $\lambda : S \to Q$ and give its coordinate matrix.
> $(d\lambda)_p(D)(f) = D(f \circ \lambda)$ for $f \in \mathcal{F}(Q)$. In coordinates it is the Jacobian $\partial(\rho^j \circ \lambda)/\partial \xi^i$, and it sends the velocity of $\gamma$ to the velocity of $\lambda \circ \gamma$.

> [!question]- ig-tan-parabola | The curve $(t, t^2)$ at $t = 1$: what are its polar components $(\dot r, \dot\theta)$?
> $(3/\sqrt2, 1/2) \approx (2.1213, 0.5)$, from $\dot r = (x\dot x + y\dot y)/r$ and $\dot\theta = (x\dot y - y\dot x)/r^2$ at $(1, 1)$ with velocity $(1, 2)$.

## Where it leads

- [Vector Fields and Tensor Fields](03-Vector-Fields-and-Tensor-Fields.md) chooses a tangent vector at every point.
- In [The Fisher Metric](../02-Geometric-Structure-of-Statistical-Models/02-The-Fisher-Metric.md) a tangent vector $\partial_i$ is represented by the score $\partial_i \ell_\xi$, a random variable; [The Geometry of P(X)](../02-Geometric-Structure-of-Statistical-Models/05-The-Geometry-of-P-of-X.md) calls this the e-representation $X^{(e)}$ and identifies $T_p$ with the zero-mean random variables $T^{(e)}_p$.
- Code: [ch1_examples.py](code/ch1_examples.py).

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 1.2.
- John M. Lee, *Introduction to Smooth Manifolds*, 2nd edition, chapter 3 (tangent vectors as derivations, the differential).
