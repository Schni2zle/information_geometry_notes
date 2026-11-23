---
type: concept
tier: core
status: solid
section: 2.5
pages: 40-45
prereqs: [the-alpha-connection, the-fisher-metric]
est_hours: 5
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 2.5, Jeffreys - An Invariant Form for the Prior Probability in Estimation Problems (Proc R Soc A 1946), Clarke and Barron - Jeffreys Prior is Asymptotically Least Favorable under Entropy Risk (JSPI 1994), Pistone and Sempi - An Infinite-Dimensional Geometric Structure on the Space of All the Probability Measures Equivalent to a Given One (Annals of Statistics 1995)]
---

# The Geometry of P(X)

## TL;DR

- For finite $\mathcal{X}$, $\mathcal{P} = \mathcal{P}(\mathcal{X})$ is an open subset of the affine space $\{\sum_xA(x) = 1\}$; every model on $\mathcal{X}$ is a submanifold, and its Fisher metric and $\alpha$-connections are projections of those of $\mathcal{P}$.
- Three ways to write a tangent vector $X$: the $m$-representation $X^{(m)} = X(p)$, a function with $\sum_xX^{(m)}(x) = 0$; the $e$-representation $X^{(e)} = X(\log p) = X^{(m)}/p$, a random variable with $E_p[X^{(e)}] = 0$; the 0-representation $X^{(0)} = X^{(m)}/\sqrt p$.
- Fisher metric: $\langle X, Y\rangle_p = E_p[X^{(e)}Y^{(e)}] = \sum_xX^{(m)}Y^{(e)} = \sum_xX^{(0)}Y^{(0)}$.
- $m$-parallel translation keeps $X^{(m)}$ fixed (2.39); $e$-parallel translation keeps $X^{(e)}$ fixed up to recentring, $X'^{(e)} = X^{(e)} - E_q[X^{(e)}]$ (2.43). Neither preserves the metric, but the pair does: $\langle\Pi^{(e)}X, \Pi^{(m)}Y\rangle_q = \langle X, Y\rangle_p$.
- $V_p[A] = \lVert(dE[A])_p\rVert^2$ (Theorem 2.7); restricted to a model, $V_p[A] \ge \lVert(dE[A]|_S)_p\rVert^2$ (Theorem 2.8), which yields Cramer-Rao and shows an efficient estimator forces an exponential family.
- $p \mapsto 2\sqrt p$ maps $\mathcal{P}$ onto part of the sphere of radius 2, and the Fisher metric is the induced Euclidean metric; Jeffreys' prior $\propto\sqrt{\det G}$ is the uniform distribution on that sphere.

## Learning objectives

- Describe $\mathcal{P}(\mathcal{X})$ for finite $\mathcal{X}$ as a manifold and identify its tangent spaces.
- Convert between the $m$-, $e$- and 0-representations, and express the Fisher metric in each.
- Compute $m$- and $e$-parallel translation and see the duality relation they satisfy.
- Define gradients and prove Theorems 2.7 and 2.8, and derive the Cramer-Rao inequality from them.
- Explain the square-root embedding, the sphere picture and Jeffreys' prior.

## Core concepts

### $\mathcal{P}$ as an open set of an affine space

Let $\mathcal{X}$ be finite.
Every model $S$ on $\mathcal{X}$ is a submanifold of $\mathcal{P} = \mathcal{P}(\mathcal{X})$, and its Fisher metric and $\alpha$-connections are the projections of those of $\mathcal{P}$ onto $S$, so the geometry of $\mathcal{P}$ is fundamental.
The book focuses on the Fisher metric and the $e$- and $m$-connections here, because they are the most important in applications and have simpler structure; they are tied to the duality of section 3.5.

$\mathcal{P}$ is an open subset of the affine subspace $\mathcal{A}_1 = \{A \mid \sum_xA(x) = 1\}$ of $\mathbb{R}^{\mathcal{X}}$, so $T_p(\mathcal{P})$ is naturally the linear subspace $\mathcal{A}_0 = \{A \mid \sum_xA(x) = 0\}$.

### The $m$-representation and the $m$-connection

Viewing $X \in T_p(\mathcal{P})$ as an element of $\mathcal{A}_0$ gives its mixture representation ($m$-representation) $X^{(m)}$:

$$
T^{(m)}_p(\mathcal{P}) = \{X^{(m)} \mid X \in T_p(\mathcal{P})\} = \mathcal{A}_0.
$$

For a coordinate basis, $(\partial_i)^{(m)}_\xi = \partial_ip_\xi$.
$\mathcal{P}$ is a mixture family, so the $m$-connection is the natural connection of the affine structure of $\mathcal{A}_1$, and $m$-parallel translation $\Pi^{(m)}_{p,q} : T_p(\mathcal{P}) \to T_q(\mathcal{P})$ is

$$
\Pi^{(m)}_{p,q}(X) = X' \iff X'^{(m)} = X^{(m)}. \tag{2.39}
$$

### The $e$-representation and the $e$-connection

Embed $\mathcal{P}$ instead as $\{\log p \mid p \in \mathcal{P}\} \subset \mathbb{R}^{\mathcal{X}}$.
$X \in T_p(\mathcal{P})$ is represented by $X$ applied to $p \mapsto \log p$, the exponential (or logarithmic) representation $X^{(e)}$; in particular $(\partial_i)^{(e)}_\xi = \partial_i\log p_\xi$, the score.
Clearly

$$
X^{(e)}(x) = X^{(m)}(x)/p(x), \tag{2.40}
$$

$$
T^{(e)}_p(\mathcal{P}) = \{X^{(e)} \mid X \in T_p(\mathcal{P})\} = \{A \in \mathbb{R}^{\mathcal{X}} \mid E_p[A] = 0\}, \tag{2.41}
$$

with $E_p[A] = \sum_xp(x)A(x)$, and the Fisher metric becomes

$$
\langle X, Y\rangle_p = E_p[X^{(e)}Y^{(e)}]. \tag{2.42}
$$

Unlike $T^{(m)}_p$, the space $T^{(e)}_p$ depends on $p$: a zero-mean random variable under $p$ is generally not zero-mean under $q$.
But $A \mapsto A - E_q[A]$ is a linear isomorphism $T^{(e)}_p \to T^{(e)}_q$, and it is $e$-parallel translation:

$$
\Pi^{(e)}_{p,q}(X) = X' \iff X'^{(e)} = X^{(e)} - E_q[X^{(e)}]. \tag{2.43}
$$

Proof: by (2.25) with $\alpha = 1$, $\langle\nabla^{(e)}_{\partial_i}X, \partial_k\rangle_p = E_p[(\partial_iX^{(e)})_p(\partial_k)^{(e)}_p]$ (2.44).
If $X^{(e)}_p = F - E_p[F]$ for a fixed random variable $F$, then $\partial_iX^{(e)} = -\partial_iE_p[F]$ is constant on $\mathcal{X}$ and has zero inner product with any score, so $X$ is $e$-parallel.
Note that $\Pi^{(e)}$ differs from the $m$-parallel translation, which in $e$-representation reads $A' = Ap/q$.

### Gradients and variance: Theorem 2.7

For a Riemannian manifold $(S, g)$ the cotangent space $T^*_p(S)$ is the dual of $T_p(S)$; $X \mapsto \omega_X = \langle X, \cdot\rangle_p$ identifies them and carries the inner product over.
The differential $(df)_p \in T^*_p$ is $X \mapsto Xf$, and the gradient $(\text{grad}\,f)_p \in T_p$ is the vector with

$$
\langle(\text{grad}\,f)_p, X\rangle_p = (df)_p(X) = Xf \qquad \forall X \in T_p(S), \tag{2.45}
$$

$$
(\text{grad}\,f)_p = (\partial_if)_pg^{ij}(p)(\partial_j)_p, \qquad \lVert(df)_p\rVert^2_p = \lVert(\text{grad}\,f)_p\rVert^2_p = (\partial_if)_p(\partial_jf)_pg^{ij}(p). \tag{2.46-2.47}
$$

**Theorem 2.7.** For $A : \mathcal{X} \to \mathbb{R}$ and $E[A] : p \mapsto E_p[A]$ on $\mathcal{P}$,

$$
V_p[A] = \lVert(dE[A])_p\rVert^2_p, \tag{2.48}
$$

with the norm from the Fisher metric: the variance of $A$ measures how sensitive its expectation is to perturbations of $p$.
Proof: for $X \in T_p(\mathcal{P})$, $X(E[A]) = \sum_xX^{(m)}(x)A(x) = E_p[X^{(e)}A] = E_p[X^{(e)}(A - E_p[A])]$ (2.49), since $E_p[X^{(e)}] = 0$.
$A - E_p[A] \in T^{(e)}_p$, so it is $Y^{(e)}_p$ for some $Y_p$, which by (2.45) and (2.49) is $(\text{grad}\,E[A])_p$; hence $\lVert dE[A]\rVert^2 = \lVert Y_p\rVert^2 = E_p[(Y^{(e)}_p)^2] = V_p[A]$.

**Theorem 2.8.** For a submodel $S \subset \mathcal{P}$,

$$
V_p[A] \ge \lVert(dE[A]|_S)_p\rVert^2_p, \tag{2.50}
$$

with equality iff

$$
A - E_p[A] \in T^{(e)}_p(S) = \{X^{(e)} \mid X \in T_p(S)\}. \tag{2.51}
$$

Proof: the gradient of $E[A]|_S$ is the orthogonal projection of $\text{grad}\,E[A]$ onto $T_p(S)$, and projections do not increase length.

### Cramer-Rao and efficient estimators, geometrically

For an unbiased estimator $\hat\xi$ on a finite $\mathcal{X}$, set $A = c_i\hat\xi^i$ for $c \in \mathbb{R}^n$.
Unbiasedness gives $E[A]|_S = c_i\xi^i$, so (2.47) and (2.50) give $c^\top V_\xi[\hat\xi]c \ge c^\top G(\xi)^{-1}c$, which is Theorem 2.2.
Equality $V_\xi[\hat\xi] = G(\xi)^{-1}$ at $p$ requires $c_i(\hat\xi^i - \xi^i(p)) \in T^{(e)}_p(S)$ for all $c$, i.e. $\hat\xi^i - \xi^i(p) \in T^{(e)}_p(S)$ for each $i$.
So if $\hat\xi$ is efficient there are $n$ vector fields $X^i$ on $S$ with $(X^i_p)^{(e)} = \hat\xi^i - \xi^i(p)$, which by (2.43) are $e$-parallel; thus $S$ is $e$-autoparallel in $\mathcal{P}$ (section 1.8), i.e. an exponential family (Theorem 2.5).
Section 3.5 completes this with a necessary and sufficient condition (Theorem 3.12).

**Locally unbiased estimators.** $\hat\xi$ is locally unbiased at $\xi$ if $E_{\xi+\Delta\xi}[\hat\xi] = \xi + \Delta\xi + o(\Delta\xi)$ (2.52), i.e. $E_\xi[\hat\xi] = \xi$ and $\partial_iE_\xi[\hat\xi^j] = \delta^j_i$ (2.53).
Unbiased means locally unbiased at every $\xi$; the Cramer-Rao inequality holds at $\xi$ for any locally unbiased estimator, and the bound is always attained at a given $\xi$ by

$$
\hat\xi^i(x) = \xi^i + g^{ij}(\xi)\partial_j\log p(x; \xi). \tag{2.54}
$$

### The 0-representation and the sphere

A third embedding is $p \mapsto 2\sqrt p$, which identifies $\mathcal{P}$ with $\{2\sqrt p \mid p \in \mathcal{P}\}$, part of the sphere $\{a \in \mathbb{R}^{\mathcal{X}} \mid \sum_x(a(x))^2 = 4\}$ of radius 2.
A tangent vector is represented by $X^{(0)} = X^{(m)}/\sqrt p = \sqrt pX^{(e)}$, its 0-representation (the general $\alpha$-representation is in section 2.6), and

$$
\langle X, Y\rangle_p = \sum_xX^{(0)}(x)Y^{(0)}(x), \tag{2.55}
$$

which is (2.10): the Fisher metric is the Riemannian metric induced on the sphere by the Euclidean metric of $\mathbb{R}^{\mathcal{X}}$.
Consequently the Levi-Civita ($\alpha = 0$) geometry of $\mathcal{P}$ is spherical, and geodesic distances are great-circle distances on the radius-2 sphere.

### Jeffreys' prior

For a model $S = \{p_\xi \mid \xi \in \Xi\}$ with Fisher matrix $G(\xi)$, suppose its Riemannian volume $V = \int_\Xi\sqrt{\det G(\xi)}\,d\xi$ is finite.
Then $Q(\xi) = \frac1V\sqrt{\det G(\xi)}$ is a probability density on $\Xi$, invariant under reparametrisation, so it is a probability distribution on $S$: Jeffreys' prior.
It is important in Bayesian statistics and in universal data compression (Clarke and Barron).
For $S = \mathcal{P}(\mathcal{X})$ with $\mathcal{X} = \{0, 1, \dots, n\}$, $V$ is the area of the $n$-sphere of radius 2 divided by $2^{n+1}$ (the positive orthant),

$$
V = \frac{\pi^{(n+1)/2}}{\Gamma(\frac{n+1}{2})},
$$

and Jeffreys' prior is the uniform distribution on the sphere.

### Infinite $\mathcal{X}$

For finite $\mathcal{X}$, $\mathcal{P}$ is open in $\mathcal{A}_1$ because $p(x) > 0$ is a mild constraint.
As $\lvert\mathcal{X}\rvert$ grows the constraint gets more restrictive, and for infinite $\mathcal{X}$, $\mathcal{P}$ cannot have the dimension of $\mathcal{A}_1$ and is not even an infinite-dimensional manifold in the usual sense; the arguments of this section lose their rigorous basis.
They do not become meaningless: Cramer-Rao for infinite $\mathcal{X}$ has an almost identical proof, though the geometric framework no longer fully applies, and in a sense $\mathcal{P}$ behaves like an infinite-dimensional exponential family.
Rigorous constructions exist (von Friedrich, Kambayashi, Lafferty, Pistone and Sempi, Gibilisco and Pistone, Pistone and Rogantin).

## Worked examples

### Three representations of one tangent vector

At $p = (0.5, 0.3, 0.2)$ take $X^{(m)} = (0.1, -0.1, 0)$ (it sums to 0).
Then $X^{(e)} = X^{(m)}/p = (0.2, -0.3333, 0)$, which has $E_p[X^{(e)}] = 0$, and $X^{(0)} = (0.1414, -0.1826, 0)$.
$\lVert X\rVert^2_p = \sum(X^{(m)})^2/p = 0.02 + 0.03333 = 0.05333$, the same from all three formulas.

### $e$- and $m$-parallel translation to another point

Translate $X$ to $q = (0.2, 0.3, 0.5)$.
$m$-translation keeps $X^{(m)} = (0.1, -0.1, 0)$, with $\lVert\Pi^{(m)}X\rVert^2_q = 0.01/0.2 + 0.01/0.3 = 0.08333$.
$e$-translation: $E_q[X^{(e)}] = 0.04 - 0.1 = -0.06$, so $X'^{(e)} = (0.26, -0.27333, 0.06)$ and $X'^{(m)} = qX'^{(e)} = (0.052, -0.082, 0.03)$, with $\lVert\Pi^{(e)}X\rVert^2_q = 0.03773$.
Neither equals the original $0.05333$: neither connection is metric.
But $\langle\Pi^{(e)}X, \Pi^{(m)}X\rangle_q = \sum_xX'^{(e)}X^{(m)} = 0.026 + 0.02733 = 0.05333$, exactly the original.
In general $\sum_x(X^{(e)} - c)Y^{(m)} = \sum_xX^{(e)}Y^{(m)}$ because $\sum_xY^{(m)} = 0$: the two translations preserve the metric jointly, the duality of chapter 3.

### Theorem 2.7 by hand

$A = (1, 2, 4)$ at $p = (0.5, 0.3, 0.2)$: $E_p[A] = 1.9$ and $V_p[A] = 0.405 + 0.003 + 0.882 = 1.29$.
In the coordinates $\xi = (p(x_1), p(x_2)) = (0.3, 0.2)$, $E[A] = A_0 + \xi^1(A_1 - A_0) + \xi^2(A_2 - A_0)$ has differential $(1, 3)$, and the inverse Fisher matrix of the multinomial is $g^{ij} = \xi^i\delta^{ij} - \xi^i\xi^j = \begin{pmatrix} 0.21 & -0.06 \\ -0.06 & 0.16\end{pmatrix}$.
$\lVert dE[A]\rVert^2 = 0.21 - 0.36 + 1.44 = 1.29$, matching (2.48).

### Jeffreys' prior and Fisher-Rao distances

For the Bernoulli family ($n = 1$), $\sqrt{\det G} = 1/\sqrt{p(1 - p)}$ integrates to $\pi = \pi^1/\Gamma(1)$, and $Q$ is the Beta$(\frac12, \frac12)$ density.
For $n = 2$ the formula gives $\pi^{3/2}/\Gamma(3/2) = 2\pi$, confirmed by integrating $1/\sqrt{p_0p_1p_2}$ over the triangle.
On the radius-2 sphere the great-circle distance is $d(p, q) = 2\arccos\sum_x\sqrt{p(x)q(x)}$ (twice the angle between $\sqrt p$ and $\sqrt q$).
For $p = (0.5, 0.3, 0.2)$ and $q = (0.2, 0.3, 0.5)$, $\sum\sqrt{pq} = 0.93246$ and $d = 0.7393$.
For Bernoulli $0.3 \to 0.6$ the formula and $\int_{0.3}^{0.6}dp/\sqrt{p(1 - p)}$ both give $0.6129$.

## Pitfalls

- Using the $e$-representation of one point at another point; $T^{(e)}_p$ depends on $p$, and a score at $p$ is not a tangent vector at $q$ until it is recentred.
- Treating $\Pi^{(e)}$ or $\Pi^{(m)}$ as isometries; only the mixed pairing $\langle\Pi^{(e)}X, \Pi^{(m)}Y\rangle$ is preserved.
- Reading Cramer-Rao as an inequality about one estimator only; geometrically it is "projection shortens vectors", and equality pins down the shape of the model.
- Computing Fisher-Rao distances as $\lVert\sqrt p - \sqrt q\rVert$; that is the chord (Hellinger-type), while the geodesic distance follows the sphere.
- Extending this section verbatim to continuous $\mathcal{X}$; $\mathcal{P}$ is then not a Banach manifold in the naive sense.

## Review questions

> [!question]- ig-px-tangent | What is $T_p(\mathcal{P})$ for finite $\mathcal{X}$, in $m$- and $e$-representation?
> $T^{(m)}_p = \{A \mid \sum_xA(x) = 0\}$ (independent of $p$) and $T^{(e)}_p = \{A \mid E_p[A] = 0\}$ (depends on $p$), related by $X^{(e)} = X^{(m)}/p$.

> [!question]- ig-px-metric-forms | Write the Fisher metric of $\mathcal{P}$ in the $e$-, mixed and 0-representations.
> $E_p[X^{(e)}Y^{(e)}] = \sum_xX^{(m)}Y^{(e)} = \sum_xX^{(0)}Y^{(0)}$, with $X^{(0)} = X^{(m)}/\sqrt p$.

> [!question]- ig-px-transport | How do $m$- and $e$-parallel translation act?
> $m$: keep $X^{(m)}$ unchanged. $e$: keep $X^{(e)}$ and recentre, $X'^{(e)} = X^{(e)} - E_q[X^{(e)}]$.

> [!question]- ig-px-dual-pairing | Show that $\langle\Pi^{(e)}X, \Pi^{(m)}Y\rangle_q = \langle X, Y\rangle_p$.
> $\langle\Pi^{(e)}X, \Pi^{(m)}Y\rangle_q = \sum_x(X^{(e)} - c)Y^{(m)}$ with $c = E_q[X^{(e)}]$, and $\sum_xY^{(m)} = 0$, so it equals $\sum_xX^{(e)}Y^{(m)} = \langle X, Y\rangle_p$.

> [!question]- ig-px-theorem-2-7 | State Theorem 2.7 and give the proof idea.
> $V_p[A] = \lVert dE[A]\rVert^2_p$. $X(E[A]) = E_p[X^{(e)}(A - E_p[A])]$, so $\text{grad}\,E[A]$ has $e$-representation $A - E_p[A]$, whose squared norm is the variance.

> [!question]- ig-px-cramer-rao | How does Theorem 2.8 give Cramer-Rao, and what does equality imply about the model?
> With $A = c_i\hat\xi^i$, unbiasedness makes $E[A]|_S = c_i\xi^i$, so $c^\top Vc \ge c^\top G^{-1}c$. Equality for all $\xi$ needs $\hat\xi^i - \xi^i \in T^{(e)}_p(S)$, i.e. $e$-parallel fields on $S$, so $S$ is $e$-autoparallel: an exponential family.

> [!question]- ig-px-sphere | What does the map $p \mapsto 2\sqrt p$ show about the Fisher metric?
> It sends $\mathcal{P}$ into the sphere of radius 2, and the Fisher metric is the induced Euclidean metric. So $\nabla^{(0)}$-geodesics are great circles and $d(p, q) = 2\arccos\sum\sqrt{pq}$.

> [!question]- ig-px-jeffreys | What is Jeffreys' prior, and what is it for $\mathcal{P}(\{0, \dots, n\})$?
> $Q(\xi) = \sqrt{\det G(\xi)}/V$, the normalised Riemannian volume, invariant under reparametrisation. For $\mathcal{P}$ it is uniform on the radius-2 sphere with $V = \pi^{(n+1)/2}/\Gamma(\frac{n+1}{2})$; for $n = 1$ it is Beta$(\frac12, \frac12)$ with $V = \pi$.

> [!question]- ig-px-local-unbiased | Which locally unbiased estimator attains the Cramer-Rao bound at a fixed $\xi$?
> $\hat\xi^i(x) = \xi^i + g^{ij}(\xi)\partial_j\log p(x; \xi)$. It depends on $\xi$, so it is not an estimator usable at every point unless the model is special.

> [!question]- ig-px-variance-example | For $A = (1, 2, 4)$ under $p = (0.5, 0.3, 0.2)$, what are $E_p[A]$, $V_p[A]$ and $\lVert dE[A]\rVert^2$?
> $1.9$, $1.29$ and $1.29$; the last uses $dE = (1, 3)$ and $g^{ij} = \xi^i\delta^{ij} - \xi^i\xi^j$ at $\xi = (0.3, 0.2)$.

## Where it leads

- [Alpha-Affine Manifolds and Alpha-Families](06-Alpha-Affine-Manifolds-and-Alpha-Families.md) generalises the $e$/$m$/0 representations to all $\alpha$.
- Chapter 3 (dual connections) turns the pairing $\langle\Pi^{(e)}X, \Pi^{(m)}Y\rangle = \langle X, Y\rangle$ into the definition of duality, and section 3.5 completes the efficient-estimator story.
- Code: [ch2_examples.py](code/ch2_examples.py).

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 2.5.
- Harold Jeffreys, "An invariant form for the prior probability in estimation problems", *Proceedings of the Royal Society A* 186 (1946).
- Bertrand Clarke and Andrew Barron, "Jeffreys' prior is asymptotically least favorable under entropy risk", *Journal of Statistical Planning and Inference* 41 (1994).
- Giovanni Pistone and Carlo Sempi, "An infinite-dimensional geometric structure on the space of all the probability measures equivalent to a given one", *Annals of Statistics* 23(5) (1995).
