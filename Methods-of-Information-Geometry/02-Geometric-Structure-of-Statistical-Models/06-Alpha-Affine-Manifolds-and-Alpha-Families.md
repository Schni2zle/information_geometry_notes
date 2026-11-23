---
type: concept
tier: advanced
status: solid
section: 2.6
pages: 45-50
prereqs: [the-geometry-of-p-of-x, the-alpha-connection, autoparallel-submanifolds]
est_hours: 4
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 2.6, Amari - Information Geometry and Its Applications (Springer 2016) ch 3 and 4, Tsallis - Possible Generalization of Boltzmann-Gibbs Statistics (J Stat Phys 1988)]
---

# Alpha-Affine Manifolds and Alpha-Families

## TL;DR

- Drop normalisation: $\tilde{\mathcal{P}}(\mathcal{X}) = \{p > 0, \int p < \infty\}$ (positive finite measures), on which $g$ and $\nabla^{(\alpha)}$ are still defined by (2.6) and (2.25), though identities like $E[\partial_i\ell] = 0$ are lost.
- The $\alpha$-embedding $\ell^{(\alpha)} = L^{(\alpha)}(p)$ with $L^{(\alpha)}(u) = \frac{2}{1 - \alpha}u^{(1-\alpha)/2}$ ($\alpha \neq 1$) and $\log u$ ($\alpha = 1$) gives the $\alpha$-representation $X^{(\alpha)} = X\ell^{(\alpha)}$; $\alpha = 1, 0, -1$ are the $e$-, 0- and $m$-representations.
- $g_{ij} = \int\partial_i\ell^{(\alpha)}\partial_j\ell^{(-\alpha)}dx$ and $\Gamma^{(\alpha)}_{ij,k} = \int\partial_i\partial_j\ell^{(\alpha)}\partial_k\ell^{(-\alpha)}dx$ (2.60)-(2.61): $\nabla^{(\alpha)}$ is the flat connection of $\mathbb{R}^{\mathcal{X}}$ pulled back by the $\alpha$-embedding, paired with the $(-\alpha)$-embedding.
- $S$ is $\alpha$-affine if $\ell^{(\alpha)}(x; \theta) = C(x) + \theta^iF_i(x)$ (2.65); mixture families are $(-1)$-affine, $\tilde{\mathcal{P}}(\mathcal{X})$ (finite) is $\alpha$-affine for every $\alpha$, exponential families are not 1-affine.
- The denormalisation $\tilde S = \{\tau p_\xi\}$ adds a scale coordinate; $S$ is always $(-1)$-autoparallel in $\tilde S$ (Theorem 2.9), and $M$ is $\alpha$-autoparallel in $S$ iff $\tilde M$ is in $\tilde S$ (Theorem 2.10).
- $S$ is an $\alpha$-family if $\tilde S$ is $\alpha$-affine, i.e. $p(x; \xi) = \{\sum_{\lambda=0}^n\theta^\lambda(\xi)F_\lambda(x)\}^{2/(1-\alpha)}$ (2.76); $\alpha = -1$ gives mixture families and $\alpha = 1$ exponential families, and sub-$\alpha$-families are exactly the $\alpha$-autoparallel submanifolds (Theorem 2.11). An $\alpha$-family need not be $\alpha$-flat.

## Learning objectives

- Define $\tilde{\mathcal{P}}(\mathcal{X})$, the $\alpha$-embeddings and the $\alpha$-representations.
- Express the Fisher metric and $\alpha$-connections through the $\pm\alpha$-representations and interpret the formula.
- Define $\alpha$-affine manifolds and decide which standard families are $\alpha$-affine.
- Compute the metric and connections of a denormalised model, and use Theorems 2.9 to 2.11.
- Write down $\alpha$-families and explain why only $\alpha = \pm1$ give flat families.

## Core concepts

### Positive finite measures

So far each $p_\xi$ was a probability distribution.
Relax this to

$$
\tilde{\mathcal{P}}(\mathcal{X}) = \left\{p : \mathcal{X} \to \mathbb{R} \;\middle|\; p(x) > 0 \;(\forall x \in \mathcal{X}), \int p(x)\,dx < \infty\right\}, \tag{2.56}
$$

and let $S = \{p_\xi\} \subset \tilde{\mathcal{P}}(\mathcal{X})$.
Keeping the other assumptions of sections 2.1 and 2.2, $S$ is a manifold and $g$ and $\nabla^{(\alpha)}$ can still be defined by (2.6) and (2.25), but (2.8) and (2.9) no longer hold.
This extension gives a more natural view of the $\alpha$-connections, and its results relate to the Tsallis entropy of statistical physics.

### $\alpha$-embeddings and $\alpha$-representations

For each $\alpha \in \mathbb{R}$ define

$$
L^{(\alpha)}(u) = \begin{cases} \frac{2}{1 - \alpha}u^{(1-\alpha)/2} & (\alpha \neq 1) \\ \log u & (\alpha = 1) \end{cases}, \qquad \ell^{(\alpha)}(x; \xi) = L^{(\alpha)}(p(x; \xi)). \tag{2.57-2.58}
$$

$\ell^{(1)} = \ell = \log p$ and $\ell^{(-1)} = p$.
For $X \in T_\xi(S)$, the function

$$
X^{(\alpha)}(x) = X\ell^{(\alpha)}(x; \xi) \tag{2.59}
$$

is the $\alpha$-representation of $X$; the $e$-, $m$- and 0-representations of section 2.5 are $\alpha = 1, -1, 0$ (the 0-embedding is $2\sqrt p$).
Since $\partial_i\ell^{(\alpha)} = p^{(1-\alpha)/2}\partial_i\ell$ and $\partial_i\partial_j\ell^{(\alpha)} = p^{(1-\alpha)/2}(\partial_i\partial_j\ell + \frac{1 - \alpha}{2}\partial_i\ell\,\partial_j\ell)$, (2.6) and (2.25) become

$$
g_{ij}(\xi) = \int\partial_i\ell^{(\alpha)}(x; \xi)\,\partial_j\ell^{(-\alpha)}(x; \xi)\,dx, \tag{2.60}
$$

$$
\Gamma^{(\alpha)}_{ij,k}(\xi) = \int\partial_i\partial_j\ell^{(\alpha)}(x; \xi)\,\partial_k\ell^{(-\alpha)}(x; \xi)\,dx. \tag{2.61}
$$

Read (2.61) as: the $\alpha$-connection is induced from the affine structure of $\mathbb{R}^{\mathcal{X}}$ through the embedding $\xi \mapsto \ell^{(\alpha)}(\cdot; \xi)$ (second derivatives of the embedded point), measured against the $(-\alpha)$-representation instead of the $\alpha$ one.
This pairing of $\alpha$ with $-\alpha$ is the root of the duality of $\pm\alpha$-connections in chapter 3.
For probability distributions, (2.8) and (2.9) become

$$
\int p^{(1+\alpha)/2}\partial_i\ell^{(\alpha)}\,dx = 0, \qquad \frac{1 + \alpha}{2}g_{ij} = -\int p^{(1+\alpha)/2}\partial_i\partial_j\ell^{(\alpha)}\,dx. \tag{2.62-2.63}
$$

### $\alpha$-affine manifolds

If some coordinate system $[\theta^i]$ has

$$
\partial_i\partial_j\ell^{(\alpha)}(x; \theta) = 0, \tag{2.64}
$$

then (2.61) gives $\Gamma^{(\alpha)} = 0$: $[\theta^i]$ is $\alpha$-affine and $S$ is $\alpha$-flat.
Such an $S$ is an $\alpha$-affine manifold.
(2.64) holds iff there are functions $C, F_1, \dots, F_n$ on $\mathcal{X}$ with

$$
\ell^{(\alpha)}(x; \theta) = C(x) + \sum_{i=1}^n\theta^iF_i(x), \tag{2.65}
$$

i.e. the $\alpha$-embedding of $S$ is an affine subspace.
By Theorem 1.1, a submanifold $M$ of an $\alpha$-affine $S$ is $\alpha$-affine iff it is $\alpha$-autoparallel in $S$.

**Example 2.9.** A mixture family is a $(-1)$-affine manifold (since $\ell^{(-1)} = p$), but an exponential family is not a 1-affine manifold: $\ell^{(1)} = C + \theta^iF_i - \psi(\theta)$ is not affine in $\theta$ because of $\psi$.

**Example 2.10.** For finite $\mathcal{X} = \{x_1, \dots, x_n\}$ let $F_i(x_j) = \delta_{ij}$; parametrise $p \in \tilde{\mathcal{P}}(\mathcal{X})$ by $\theta^i = L^{(\alpha)}(p(x_i))$, so $L^{(\alpha)}(p(x)) = \theta^iF_i(x)$. Hence $\tilde{\mathcal{P}}(\mathcal{X})$ is $\alpha$-affine for every $\alpha$.

### Denormalisation

For infinite $\mathcal{X}$, $\tilde{\mathcal{P}}(\mathcal{X})$ is not a manifold, but informally it behaves like an $\alpha$-affine manifold.
For a model $S = \{p_\xi\} \subset \mathcal{P}(\mathcal{X})$ of probability distributions define

$$
\tilde S = \{\tau p_\xi \mid \xi \in \Xi, \tau > 0\} \subset \tilde{\mathcal{P}}(\mathcal{X}), \tag{2.66}
$$

an $(n + 1)$-dimensional manifold containing $S$ (at $\tau = 1$) as a submanifold: the denormalisation of $S$, a cone over $S$ (Figure 2.1).
Use coordinates $[\xi, \tau] = [\xi^1, \dots, \xi^n, \tau]$ with basis $\tilde\partial_i = \partial/\partial \xi^i$ and $\tilde\partial_\tau = \partial/\partial \tau$, and lift a vector field $X = X^i\partial_i$ on $S$ to $\tilde X = X^i\tilde\partial_i$.
From $\tilde\ell^{(\alpha)} = L^{(\alpha)}(\tau p(x; \xi)) = \tau^{(1-\alpha)/2}\ell^{(\alpha)}$ and (2.60)-(2.61):

$$
\tilde g_{ij} = \tau g_{ij}, \qquad \tilde g_{i\tau} = 0, \qquad \tilde g_{\tau\tau} = \tau^{-1}, \tag{2.67}
$$

$$
\tilde\Gamma^{(\alpha)}_{ij,k} = \tau\Gamma^{(\alpha)}_{ij,k}, \qquad \tilde\Gamma^{(\alpha)}_{ij,\tau} = -\frac{1 + \alpha}{2}g_{ij}, \tag{2.68}
$$

$$
\tilde\Gamma^{(\alpha)}_{i\tau,k} = \tilde\Gamma^{(\alpha)}_{\tau i,k} = \frac{1 - \alpha}{2}g_{ik}, \qquad \tilde\Gamma^{(\alpha)}_{i\tau,\tau} = \tilde\Gamma^{(\alpha)}_{\tau i,\tau} = 0, \tag{2.69}
$$

$$
\tilde\Gamma^{(\alpha)}_{\tau\tau,k} = 0, \qquad \tilde\Gamma^{(\alpha)}_{\tau\tau,\tau} = -\frac{1 + \alpha}{2}\tau^{-2}. \tag{2.70}
$$

In terms of covariant derivatives (with $\widetilde{(\cdot)}$ the lift):

$$
\tilde\nabla^{(\alpha)}_{\tilde X}\tilde Y = \widetilde{(\nabla^{(\alpha)}_XY)} - \frac{1 + \alpha}{2}\langle\tilde X, \tilde Y\rangle\tilde\partial_\tau, \tag{2.71}
$$

$$
\tilde\nabla^{(\alpha)}_{\tilde X}\tilde\partial_\tau = \tilde\nabla^{(\alpha)}_{\tilde\partial_\tau}\tilde X = \frac{1 - \alpha}{2}\tau^{-1}\tilde X, \qquad \tilde\nabla^{(\alpha)}_{\tilde\partial_\tau}\tilde\partial_\tau = -\frac{1 + \alpha}{2}\tau^{-1}\tilde\partial_\tau, \tag{2.72-2.73}
$$

where $\langle\tilde X, \tilde Y\rangle$ is taken with $\tilde g$.

**Theorem 2.9.** $S$ is $(-1)$-autoparallel in $\tilde S$.
(At $\alpha = -1$ the normal term in (2.71) vanishes; equivalently, normalising is a linear constraint on the $m$-representation.)

**Theorem 2.10.** For a submanifold $M$ of $S$ with denormalisation $\tilde M$ and any $\alpha$: $M$ is $\alpha$-autoparallel in $S$ iff $\tilde M$ is $\alpha$-autoparallel in $\tilde S$.
Proof: a vector field on $\tilde M$ is $f^i\tilde X_i + f^0\tilde\partial_\tau|_{\tilde M}$ with $X_i$ on $M$; by (2.72)-(2.73) the condition reduces to $\tilde\nabla^{(\alpha)}_{\tilde X}\tilde Y \in \mathcal{T}(\tilde M)$, and by (2.71) $\tilde\nabla^{(\alpha)}_{\tilde X}\tilde Y \in \mathcal{T}(\tilde M) \iff (\nabla^{(\alpha)}_XY)^\sim \in \mathcal{T}(\tilde M) \iff \nabla^{(\alpha)}_XY \in \mathcal{T}(M)$.

### $\alpha$-families

A model $S$ whose denormalisation $\tilde S$ is an $\alpha$-affine manifold is an $\alpha$-family.

**Example 2.11.** For finite $\mathcal{X}$, $\mathcal{P}(\mathcal{X})$ is an $\alpha$-family for every $\alpha$ (its denormalisation is $\tilde{\mathcal{P}}(\mathcal{X})$, Example 2.10).

For an $\alpha$-family, (2.65) on $\tilde S$ reads

$$
L^{(\alpha)}(\tau p(x; \xi)) = C(x) + \sum_{\lambda=0}^n\theta^\lambda F_\lambda(x), \tag{2.74}
$$

with $[\xi^1, \dots, \xi^n, \tau] \leftrightarrow [\theta^0, \dots, \theta^n]$ one-to-one.
For $\alpha \neq 1$, letting $\tau \to 0$ ($\alpha < 1$) or $\tau \to \infty$ ($\alpha > 1$) shows the affine space spanned by $L^{(\alpha)}(\tau p)$ contains the origin, so it is linear and $C = 0$:

$$
\ell^{(\alpha)}(x; \xi) = \sum_{\lambda=0}^n\theta^\lambda(\xi)F_\lambda(x), \qquad p(x; \xi) = \left\{\sum_{\lambda=0}^n\theta^\lambda(\xi)F_\lambda(x)\right\}^{2/(1-\alpha)} \tag{2.75-2.76}
$$

(rescaling $\theta^\lambda$ by a constant).

**Example 2.12 ($\alpha = -1$).** (2.76) becomes a mixture family: with $F_i - (a_i/a_0)F_0$ for $1 \le i \le n$ and $F_0/a_0$, where $a_\lambda = \int F_\lambda\,dx$, it is rewritten as (2.35). A $(-1)$-family is a mixture family and vice versa, consistent with Theorem 2.9.

**Example 2.13 ($\alpha = 1$).** A 1-family is an exponential family and vice versa: $L^{(1)}(\tau p) = \log p + \log\tau$, so choosing $F_0 = 1$ in (2.74) and $\theta^0 = \psi(\theta^1, \dots, \theta^n)$ gives (2.31).

**Theorem 2.11.** Let $S$ be an $\alpha$-family. A submanifold $M$ is an $\alpha$-family iff it is $\alpha$-autoparallel in $S$.
(From Theorem 2.10; it generalises Theorem 2.5.)
In particular, for finite $\mathcal{X}$ the $\alpha$-families on $\mathcal{X}$ are exactly the $\alpha$-autoparallel submanifolds of $\mathcal{P}(\mathcal{X})$.

### Why $\alpha = \pm1$ are special

Unlike Theorem 2.5, Theorem 2.4 has no $\alpha$-version: an $\alpha$-family is not $\alpha$-flat in general.
For $\alpha = -1$ the reason is Theorem 2.9: a $(-1)$-family inherits $(-1)$-flatness from $\tilde S$ because it sits in it autoparallelly.
For $\alpha = 1$, flatness can be understood from Theorem 2.9 together with the duality between the $\pm1$-connections (section 3.5).
For other $\alpha$, $S$ is a curved slice of the flat cone $\tilde S$.

## Worked examples

### $\alpha$-representations of one vector

At $p = (0.5, 0.3, 0.2)$, the vector with $X^{(m)} = (0.1, -0.1, 0)$ has $X^{(\alpha)} = p^{(1-\alpha)/2}X^{(e)}$:

- $\alpha = 1$: $(0.2, -0.3333, 0)$;
- $\alpha = 0$: $(0.1414, -0.1826, 0)$;
- $\alpha = -1$: $(0.1, -0.1, 0)$.

For any $\alpha$ (checked at $\alpha = 0.5, 2, -3$), $\sum_xX^{(\alpha)}X^{(-\alpha)} = \sum_xp\,(X^{(e)})^2 = 0.05333$, which is (2.60).

### The denormalised Bernoulli family

$\tilde S = \{\tau(1 - \xi), \tau\xi\}$ is all of $\tilde{\mathcal{P}}(\{0, 1\})$.
Computing (2.60)-(2.61) directly at $\alpha = 1/3$ gives $\tilde g = \text{diag}(\tau/(\xi(1 - \xi)), 1/\tau)$, $\tilde\Gamma_{\tau\tau,\tau} = -\frac23\tau^{-2}$, $\tilde\Gamma_{\xi\xi,\tau} = -\frac23g_{\xi\xi}$ and $\tilde\Gamma_{\xi\tau,\xi} = \frac13g_{\xi\xi}$, exactly (2.67)-(2.70) with $(1 + \alpha)/2 = 2/3$ and $(1 - \alpha)/2 = 1/3$.

### Three curves between two distributions

Join $p_0 = (0.5, 0.3, 0.2)$ and $p_1 = (0.2, 0.3, 0.5)$ by the 1-dimensional $\alpha$-family through them, $p_t \propto\{(1 - t)p_0^{(1-\alpha)/2} + tp_1^{(1-\alpha)/2}\}^{2/(1-\alpha)}$ (and $p_t \propto p_0^{1-t}p_1^t$ for $\alpha = 1$).
By Theorem 2.11 each is $\alpha$-autoparallel in $\mathcal{P}(\mathcal{X})$, a geodesic of $\nabla^{(\alpha)}$ up to parametrisation.
At $t = 1/2$:

| $\alpha$ | curve | midpoint |
| :--- | :--- | :--- |
| $-1$ | mixture, $\frac12(p_0 + p_1)$ | $(0.35, 0.3, 0.35)$ |
| $0$ | $\sqrt p$ linear, normalised | $(0.3448, 0.3105, 0.3448)$ |
| $1$ | geometric mean, normalised | $(0.3391, 0.3217, 0.3391)$ |

The $\alpha = 0$ curve lies on the great circle of the radius-2 sphere through $2\sqrt{p_0}$ and $2\sqrt{p_1}$; its midpoint is at Fisher-Rao distance $0.7393/2$ from each end, as computed in [The Geometry of P(X)](05-The-Geometry-of-P-of-X.md).
"Three reasonable ways to average two distributions, and each is a straight line for a different connection."

## Pitfalls

- Expecting an $\alpha$-family to be $\alpha$-flat; $\mathcal{P}(\mathcal{X})$ is a 0-family but is a piece of a sphere, curved for $\nabla^{(0)}$.
- Forgetting that (2.8), (2.9) fail on $\tilde{\mathcal{P}}$; with unnormalised measures the score need not have mean zero.
- Calling an exponential family 1-affine; it is 1-flat (Theorem 2.4) but its 1-embedding $\log p$ is affine only up to the normaliser $\psi(\theta)$, so only its denormalisation is 1-affine.
- Mixing $\alpha$ and $-\alpha$ in (2.61); the second derivative uses the $\alpha$-embedding and the test direction the $(-\alpha)$-embedding.
- Reading $t$ in the interpolation formulas as an affine parameter; the curves are $\alpha$-autoparallel, but their natural parameter generally differs from $t$.

## Review questions

> [!question]- ig-af-embedding | Define $L^{(\alpha)}$ and the $\alpha$-representation of a tangent vector.
> $L^{(\alpha)}(u) = \frac{2}{1 - \alpha}u^{(1-\alpha)/2}$ for $\alpha \neq 1$ and $\log u$ for $\alpha = 1$; $X^{(\alpha)} = X\,L^{(\alpha)}(p)$, which equals $p^{(1-\alpha)/2}X^{(e)}$. $\alpha = 1, 0, -1$ give the $e$-, 0- and $m$-representations.

> [!question]- ig-af-metric-connection | Express $g_{ij}$ and $\Gamma^{(\alpha)}_{ij,k}$ through $\alpha$-embeddings.
> $g_{ij} = \int\partial_i\ell^{(\alpha)}\partial_j\ell^{(-\alpha)}dx$ and $\Gamma^{(\alpha)}_{ij,k} = \int\partial_i\partial_j\ell^{(\alpha)}\partial_k\ell^{(-\alpha)}dx$. The $\alpha$-connection is the flat connection of $\mathbb{R}^{\mathcal{X}}$ seen through the $\alpha$-embedding, paired with the $(-\alpha)$-embedding.

> [!question]- ig-af-affine | When is a manifold of positive measures $\alpha$-affine?
> When $\ell^{(\alpha)}(x; \theta) = C(x) + \theta^iF_i(x)$ for some coordinates, equivalently $\partial_i\partial_j\ell^{(\alpha)} = 0$; then $\Gamma^{(\alpha)} = 0$ in $\theta$.

> [!question]- ig-af-exp-not-affine | Is an exponential family a 1-affine manifold? Is it 1-flat?
> Not 1-affine: $\log p = C + \theta^iF_i - \psi(\theta)$ is not affine in $\theta$. But it is 1-flat (Theorem 2.4), and its denormalisation is 1-affine.

> [!question]- ig-af-denormalisation | What are $\tilde g$ and the key connection coefficients of the denormalisation $\tilde S = \{\tau p_\xi\}$?
> $\tilde g_{ij} = \tau g_{ij}$, $\tilde g_{i\tau} = 0$, $\tilde g_{\tau\tau} = 1/\tau$; $\tilde\Gamma_{ij,\tau} = -\frac{1 + \alpha}{2}g_{ij}$, $\tilde\Gamma_{i\tau,k} = \frac{1 - \alpha}{2}g_{ik}$, $\tilde\Gamma_{\tau\tau,\tau} = -\frac{1 + \alpha}{2}\tau^{-2}$.

> [!question]- ig-af-theorem-2-9 | Why is $S$ always $(-1)$-autoparallel in its denormalisation?
> By (2.71) the component of $\tilde\nabla^{(\alpha)}_{\tilde X}\tilde Y$ along $\tilde\partial_\tau$ is $-\frac{1 + \alpha}{2}\langle\tilde X, \tilde Y\rangle$, which vanishes at $\alpha = -1$. Normalisation is a linear constraint in the $m$-representation.

> [!question]- ig-af-alpha-family | What is an $\alpha$-family, and what is its general form?
> A model whose denormalisation is $\alpha$-affine. For $\alpha \neq 1$, $p(x; \xi) = \{\sum_{\lambda=0}^n\theta^\lambda(\xi)F_\lambda(x)\}^{2/(1-\alpha)}$; $\alpha = -1$ gives mixture families and $\alpha = 1$ exponential families.

> [!question]- ig-af-theorem-2-11 | State Theorem 2.11 and its finite-set consequence.
> In an $\alpha$-family $S$, a submanifold is an $\alpha$-family iff it is $\alpha$-autoparallel. For finite $\mathcal{X}$, the $\alpha$-families are exactly the $\alpha$-autoparallel submanifolds of $\mathcal{P}(\mathcal{X})$.

> [!question]- ig-af-not-flat | Why are only $\alpha = \pm1$ families flat in general?
> $\tilde S$ is $\alpha$-flat, but $S$ inherits flatness only if it is $\alpha$-autoparallel in $\tilde S$, which Theorem 2.9 gives for $\alpha = -1$; $\alpha = 1$ follows by duality. For $\alpha = 0$, $\mathcal{P}(\mathcal{X})$ is a curved piece of a sphere.

> [!question]- ig-af-midpoints | What are the $\alpha = -1, 0, 1$ midpoints of $(0.5, 0.3, 0.2)$ and $(0.2, 0.3, 0.5)$?
> $m$: $(0.35, 0.3, 0.35)$. $0$: normalised $((\sqrt{p_0} + \sqrt{p_1})/2)^2 = (0.3448, 0.3105, 0.3448)$. $e$: normalised $\sqrt{p_0p_1} = (0.3391, 0.3217, 0.3391)$.

## Where it leads

- Chapter 3 (dual connections) explains the $\pm\alpha$ pairing in (2.60)-(2.61) as duality, and section 3.6 develops the dualistic structure of $\alpha$-affine manifolds and $\alpha$-families with $\alpha$-divergences.
- Code: [ch2_examples.py](code/ch2_examples.py) checks (2.67)-(2.70) symbolically and computes the three midpoints.

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 2.6.
- Shun-ichi Amari, *Information Geometry and Its Applications*, Springer 2016, chapters 3 ($\alpha$-divergences, invariance) and 4 ($\alpha$-geometry, Tsallis $q$-entropy).
- Constantino Tsallis, "Possible generalization of Boltzmann-Gibbs statistics", *Journal of Statistical Physics* 52 (1988).
