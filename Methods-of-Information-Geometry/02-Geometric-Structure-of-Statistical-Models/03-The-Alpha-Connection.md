---
type: concept
tier: core
status: solid
section: 2.3
pages: 32-36
prereqs: [the-fisher-metric, affine-connections-and-covariant-derivatives, autoparallel-submanifolds]
est_hours: 5
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 2.3, Amari - Information Geometry and Its Applications (Springer 2016) ch 2 and 6, Efron - Defining the Curvature of a Statistical Problem (Annals of Statistics 1975), Dawid - Discussion of Efron 1975]
---

# The Alpha-Connection

## TL;DR

- For every real $\alpha$, $\Gamma^{(\alpha)}_{ij,k} = E_\xi[(\partial_i\partial_j\ell + \frac{1 - \alpha}{2}\partial_i\ell\,\partial_j\ell)\partial_k\ell]$ (2.25) defines a symmetric connection $\nabla^{(\alpha)}$ through $\langle\nabla^{(\alpha)}_{\partial_i}\partial_j, \partial_k\rangle = \Gamma^{(\alpha)}_{ij,k}$ (2.26).
- They differ by a symmetric cubic tensor, $\Gamma^{(\beta)}_{ij,k} = \Gamma^{(\alpha)}_{ij,k} + \frac{\alpha - \beta}{2}T_{ijk}$ with $T_{ijk} = E[\partial_i\ell\,\partial_j\ell\,\partial_k\ell]$ (2.27)-(2.28), and $\nabla^{(\alpha)} = \frac{1 + \alpha}{2}\nabla^{(1)} + \frac{1 - \alpha}{2}\nabla^{(-1)}$ (2.29).
- Theorem 2.3: $\nabla^{(0)}$ is the Levi-Civita connection of the Fisher metric; $\nabla^{(\alpha)}$ for $\alpha \neq 0$ is not metric (when $T \neq 0$).
- An exponential family $p = \exp[C + \theta^iF_i - \psi(\theta)]$ has $\Gamma^{(1)}_{ij,k} = 0$ in natural parameters: it is $e$-flat ($\nabla^{(1)} = \nabla^{(e)}$). A mixture family $p = C + \theta^iF_i$ has $\Gamma^{(-1)} = 0$: it is $m$-flat ($\nabla^{(-1)} = \nabla^{(m)}$) (Theorem 2.4).
- Theorem 2.5: a submanifold of an exponential (mixture) family is itself an exponential (mixture) family iff it is $e$-autoparallel ($m$-autoparallel). Non-autoparallel ones are curved exponential families, the subject of chapter 4.

## Learning objectives

- Define the $\alpha$-connections and the skewness tensor $T$, and relate connections with different $\alpha$.
- Prove that $\nabla^{(0)}$ is the Levi-Civita connection of the Fisher metric.
- Recognise exponential and mixture families and write the standard distributions in exponential-family form.
- Prove that exponential families are $e$-flat and mixture families $m$-flat, with natural and mixture parameters as affine coordinates.
- Use Theorem 2.5 to decide whether a submodel is an exponential family.

## Core concepts

### Definition

For a model $S = \{p_\xi\}$ and any $\alpha \in \mathbb{R}$, define the $n^3$ functions

$$
(\Gamma^{(\alpha)}_{ij,k})_\xi = E_\xi\left[\left(\partial_i\partial_j\ell_\xi + \frac{1 - \alpha}{2}\partial_i\ell_\xi\,\partial_j\ell_\xi\right)(\partial_k\ell_\xi)\right]. \tag{2.25}
$$

They transform by (1.61), so with the Fisher metric $g$ they define a connection $\nabla^{(\alpha)}$:

$$
\langle\nabla^{(\alpha)}_{\partial_i}\partial_j, \partial_k\rangle = \Gamma^{(\alpha)}_{ij,k}. \tag{2.26}
$$

$\nabla^{(\alpha)}$ is the $\alpha$-connection; it is symmetric because (2.25) is symmetric in $i, j$.
"Flat", "affine", "parallel", "autoparallel" with respect to $\nabla^{(\alpha)}$ are abbreviated $\alpha$-flat, $\alpha$-affine, and so on.

### Relations between different $\alpha$

$$
\Gamma^{(\beta)}_{ij,k} = \Gamma^{(\alpha)}_{ij,k} + \frac{\alpha - \beta}{2}T_{ijk}, \tag{2.27}
$$

$$
(T_{ijk})_\xi = E_\xi[\partial_i\ell_\xi\,\partial_j\ell_\xi\,\partial_k\ell_\xi], \tag{2.28}
$$

where $T$ is a covariant symmetric tensor of degree 3 (unrelated to torsion $T^k_{ij}$; the $\alpha$-connections are torsion-free).
In particular

$$
\nabla^{(\alpha)} = (1 - \alpha)\nabla^{(0)} + \alpha\nabla^{(1)} = \frac{1 + \alpha}{2}\nabla^{(1)} + \frac{1 - \alpha}{2}\nabla^{(-1)}, \tag{2.29}
$$

affine combinations as in the last paragraph of section 1.6.
For a submanifold $M \subset S$, the $\alpha$-connection of $M$ (defined intrinsically by (2.25) on $M$) equals the projection of the $\alpha$-connection of $S$ onto $M$ with respect to $g$ (section 1.9).

### Theorem 2.3: the 0-connection is the Riemannian connection

Differentiate $g_{ij} = E[\partial_i\ell\,\partial_j\ell]$:

$$
\partial_kg_{ij} = E[(\partial_k\partial_i\ell)(\partial_j\ell)] + E[(\partial_i\ell)(\partial_k\partial_j\ell)] + E[(\partial_i\ell)(\partial_j\ell)(\partial_k\ell)] = \Gamma^{(0)}_{ki,j} + \Gamma^{(0)}_{kj,i}, \tag{2.30}
$$

because $\Gamma^{(0)}_{ki,j} = E[\partial_k\partial_i\ell\,\partial_j\ell] + \frac12T_{kij}$ and the two halves of $T$ add up to the third term.
This is the metric condition (1.66), and $\nabla^{(0)}$ is symmetric, so:

**Theorem 2.3.** The 0-connection is the Riemannian connection with respect to the Fisher metric.

For $\alpha \neq 0$, $\nabla^{(\alpha)}$ is not metric in general.
What survives is the pair condition $\partial_kg_{ij} = \Gamma^{(\alpha)}_{ki,j} + \Gamma^{(-\alpha)}_{kj,i}$, the duality of chapter 3.

### Exponential families

If $S = \{p_\theta \mid \theta \in \Theta\}$ can be written with functions $C, F_1, \dots, F_n$ on $\mathcal{X}$ and $\psi$ on $\Theta$ as

$$
p(x; \theta) = \exp\left[C(x) + \sum_{i=1}^n\theta^iF_i(x) - \psi(\theta)\right], \tag{2.31}
$$

$S$ is an exponential family with natural (canonical) parameters $\theta$, and normalisation gives

$$
\psi(\theta) = \log\int\exp\left[C(x) + \sum_i\theta^iF_i(x)\right]dx. \tag{2.32}
$$

$\theta \mapsto p_\theta$ is injective iff $F_1, \dots, F_n, 1$ are linearly independent, which is always assumed.
Since $\partial_i\ell = F_i(x) - \partial_i\psi(\theta)$ and

$$
\partial_i\partial_j\ell(x; \theta) = -\partial_i\partial_j\psi(\theta) \tag{2.33-2.34}
$$

does not depend on $x$, (2.25) gives $\Gamma^{(1)}_{ij,k} = -\partial_i\partial_j\psi\,E_\theta[\partial_k\ell] = 0$ by (2.9).
So $[\theta^i]$ is a 1-affine coordinate system and $S$ is 1-flat.
$\nabla^{(1)}$ is called the exponential connection or $e$-connection, $\nabla^{(e)}$.
Also $g_{ij} = \partial_i\partial_j\psi(\theta)$ by (2.8), and $T_{ijk} = \partial_i\partial_j\partial_k\psi(\theta)$.

### Mixture families

If $S$ can be written as

$$
p(x; \theta) = C(x) + \sum_{i=1}^n\theta^iF_i(x), \tag{2.35}
$$

so that $S$ is an affine subspace of $\mathcal{P}(\mathcal{X})$, it is a mixture family with mixture parameters $\theta$.
The typical case mixes $n + 1$ distributions:

$$
p(x; \theta) = \sum_{i=1}^n\theta^ip_i(x) + \left(1 - \sum_{i=1}^n\theta^i\right)p_0(x) = p_0(x) + \sum_{i=1}^n\theta^i\{p_i(x) - p_0(x)\}, \tag{2.36}
$$

with $\theta^i > 0$ and $\sum\theta^i < 1$; $\mathcal{P}(\{x_0, \dots, x_n\})$ is this with point masses $p_i(x_j) = \delta_{ij}$.
For a mixture family

$$
\partial_i\ell = \frac{F_i(x)}{p(x; \theta)}, \qquad \partial_i\partial_j\ell = -\frac{F_i(x)F_j(x)}{p(x; \theta)^2}, \tag{2.37-2.38}
$$

so $\partial_i\partial_j\ell + \partial_i\ell\,\partial_j\ell = 0$ and $\Gamma^{(-1)}_{ij,k} = 0$: $[\theta^i]$ is $(-1)$-affine and $S$ is $(-1)$-flat.
$\nabla^{(-1)}$ is the mixture connection or $m$-connection, $\nabla^{(m)}$.

**Theorem 2.4.** An exponential family (mixture family) is $e$-flat ($m$-flat), and its natural parameters (mixture parameters) form an $e$-affine ($m$-affine) coordinate system.

Section 3.3 shows that an exponential family is also $m$-flat and a mixture family also $e$-flat, a consequence of the duality between the two connections.

### Theorem 2.5: autoparallel submanifolds

**Theorem 2.5.** Let $S$ be an exponential family (mixture family) and $M$ a submanifold. Then $M$ is an exponential family (mixture family) iff $M$ is $e$-autoparallel ($m$-autoparallel) in $S$.

Proof of "exponential implies $e$-autoparallel": write $q(x; u) = p(x; \theta(u)) = \exp[D(x) + u^aG_a(x) - \varphi(u)]$.
Then $G_a(x) - \partial_a\varphi(u) = \partial_a\log p(x; \theta(u)) = (\partial_a\theta^i)_u\{F_i(x) - \partial_i\psi(\theta(u))\}$, so $(\partial_a\theta^i)_uF_i(x) + \lambda_a(u) = G_a(x)$ with $\lambda_a$ independent of $x$.
Since $G_a$ does not depend on $u$ and $F_1, \dots, F_n, 1$ are independent, $(\partial_a\theta^i)_u$ is constant: $\theta(u)$ is affine in $u$, and Theorem 1.1 gives $e$-autoparallel.
The remaining parts follow from Theorem 1.1 similarly.

A submanifold of an exponential family is a curved exponential family; it plays the leading role in chapter 4, and how far it is from an exponential family is measured by its embedding curvature with respect to the $e$-connection (section 4.5), Efron's statistical curvature.

### A model that is $\alpha$-flat for every $\alpha$

Let $q$ be a smooth density on $\mathbb{R}$, $q^{(k)}(y) = q(y_1)\cdots q(y_k)$ its i.i.d. extension, and for a regular $A \in \mathbb{R}^{k \times k}$ and $\mu \in \mathbb{R}^k$ set $p_{A,\mu}(x) = q^{(k)}(A^{-1}(x - \mu))/\lvert\det A\rvert$ (the law of $AY + \mu$).
Fixing $A$, $S = \{p_{A,\mu} \mid \mu \in \mathbb{R}^k\}$ is in general neither exponential nor mixture, but it is $\alpha$-flat for every $\alpha$ and Euclidean for the Fisher metric, with $\mu$ (and its regular affine transformations) as an affine coordinate system.
Reason: $S$ is essentially the direct product of $k$ copies of the 1-dimensional location model $\{q(y - \nu)\}$, on which every connection is flat (section 1.7); for $q = N(0, 1)$ this gives the multivariate normal with fixed $\Sigma = AA^\top$.
If $q$ is even, $T = 0$ and all $\alpha$-connections coincide.

## Worked examples

### Standard exponential families

| Family | $C(x)$ | $F(x)$ | $\theta$ | $\psi(\theta)$ |
| :--- | :--- | :--- | :--- | :--- |
| Normal (2.5) | 0 | $(x, x^2)$ | $(\mu/\sigma^2, -1/(2\sigma^2))$ | $-\frac{(\theta^1)^2}{4\theta^2} + \frac12\log(-\frac{\pi}{\theta^2})$ |
| Poisson (2.7) | $-\log x!$ | $x$ | $\log\xi$ | $e^\theta$ |
| $\mathcal{P}(\mathcal{X})$ finite (2.8) | 0 | $F_i(x) = \delta(x = x_i)$ | $\log\frac{p(x_i)}{p(x_0)}$ | $\log(1 + \sum_ie^{\theta^i})$ |

For the multivariate normal (Example 2.6), $\theta^A = \Sigma^{-1}\mu$ and $\theta^B = -\frac12\Sigma^{-1}$ with $F_A = x$, $F_B = xx^\top$, and $\psi = \frac12\mu^\top\Sigma^{-1}\mu + \frac12\log\det(2\pi\Sigma)$.
Check the normal row at $(\mu, \sigma) = (1, 2)$: $\theta = (0.25, -0.125)$ and $\psi = 0.125 + \log(2\sqrt{2\pi}) = 1.7371$, equal to $\frac{\mu^2}{2\sigma^2} + \log(\sqrt{2\pi}\sigma)$.
Its Hessian in $\theta$, transformed back to $(\mu, \sigma)$ by (1.22), is $\text{diag}(1/\sigma^2, 2/\sigma^2)$, the Fisher metric.

### The $\alpha$-connections of the normal family in $(\mu, \sigma)$

Gaussian moments give $T_{\mu\mu\sigma} = 2/\sigma^3$ (and its permutations), $T_{\sigma\sigma\sigma} = 8/\sigma^3$, all other components 0, and

| | $\Gamma_{\mu\mu,\sigma}$ | $\Gamma_{\mu\sigma,\mu} = \Gamma_{\sigma\mu,\mu}$ | $\Gamma_{\sigma\sigma,\sigma}$ | others |
| :--- | ---: | ---: | ---: | ---: |
| $\alpha = 0$ (Levi-Civita) | $1/\sigma^3$ | $-1/\sigma^3$ | $-2/\sigma^3$ | 0 |
| $\alpha = 1$ ($e$) | 0 | $-2/\sigma^3$ | $-6/\sigma^3$ | 0 |
| $\alpha = -1$ ($m$) | $2/\sigma^3$ | 0 | $2/\sigma^3$ | 0 |

The rows satisfy (2.27), the $\alpha = 0$ row agrees with the Christoffel symbols of section 1.10, and the metric condition fails for $\alpha = 1$ but holds for the pair: $\partial_\sigma g_{\mu\mu} = -2/\sigma^3 = \Gamma^{(1)}_{\sigma\mu,\mu} + \Gamma^{(-1)}_{\sigma\mu,\mu}$.
$\Gamma^{(1)} \neq 0$ in $(\mu, \sigma)$ even though the family is $e$-flat: $(\mu, \sigma)$ is not an $e$-affine coordinate system; $\theta$ is.

### Bernoulli: $m$-affine in $p$, $e$-affine in $\theta$

In the mean parameter $p$, $T = E[(\partial_p\ell)^3] = (1 - 2p)/(p^2(1 - p)^2)$ (9.0703 at $p = 0.3$) and $\Gamma^{(\alpha)}_{pp,p} = -\frac{1 + \alpha}{2}T$, which vanishes for $\alpha = -1$: $p$ is a mixture parameter.
In $\theta = \log(p/(1 - p))$, $\partial^2_\theta\ell = -p(1 - p)$ is non-random and $\Gamma^{(1)} = 0$.

### Which submodels of the normal family are exponential families?

$\{N(\mu, 1)\}$ is the line $\theta^2 = -1/2$ in natural parameters: affine, so $e$-autoparallel and an exponential family (Theorem 2.5).
$\{N(\mu, \mu^2)\}$ is the parabola $\theta^2 = -(\theta^1)^2/2$: not affine, so a curved exponential family.

## Pitfalls

- Concluding that a family is not $e$-flat because $\Gamma^{(1)} \neq 0$ in some parametrisation; flatness needs some coordinates with $\Gamma = 0$.
- Confusing the skewness tensor $T_{ijk}$ with the torsion $T^k_{ij}$; all $\alpha$-connections are torsion-free.
- Assuming the $\alpha = 0$ connection is the "right" one; $e$- and $m$-connections are the ones that make estimation and testing geometry linear.
- Forgetting the independence of $F_1, \dots, F_n, 1$; without it the natural parameters are not identifiable.
- Thinking an exponential family is $e$-flat only; it is also $m$-flat, with the expectation parameters $\eta_i = E[F_i]$ as $m$-affine coordinates (section 3.3).

## Review questions

> [!question]- ig-ac-definition | Define $\Gamma^{(\alpha)}_{ij,k}$.
> $E_\xi[(\partial_i\partial_j\ell + \frac{1 - \alpha}{2}\partial_i\ell\,\partial_j\ell)\partial_k\ell]$, and $\nabla^{(\alpha)}$ is the connection with $\langle\nabla^{(\alpha)}_{\partial_i}\partial_j, \partial_k\rangle = \Gamma^{(\alpha)}_{ij,k}$ for the Fisher metric.

> [!question]- ig-ac-skewness | How are $\Gamma^{(\alpha)}$ and $\Gamma^{(\beta)}$ related?
> $\Gamma^{(\beta)}_{ij,k} = \Gamma^{(\alpha)}_{ij,k} + \frac{\alpha - \beta}{2}T_{ijk}$ with $T_{ijk} = E[\partial_i\ell\,\partial_j\ell\,\partial_k\ell]$; equivalently $\nabla^{(\alpha)} = \frac{1 + \alpha}{2}\nabla^{(e)} + \frac{1 - \alpha}{2}\nabla^{(m)}$.

> [!question]- ig-ac-theorem-2-3 | Prove that $\nabla^{(0)}$ is the Levi-Civita connection of the Fisher metric.
> $\partial_kg_{ij} = E[\partial_k\partial_i\ell\,\partial_j\ell] + E[\partial_i\ell\,\partial_k\partial_j\ell] + T_{kij}$, and splitting $T$ in half gives $\Gamma^{(0)}_{ki,j} + \Gamma^{(0)}_{kj,i}$, the metric condition. It is symmetric, so by uniqueness it is the Levi-Civita connection.

> [!question]- ig-ac-exp-flat | Why is an exponential family $e$-flat?
> In natural parameters $\partial_i\partial_j\ell = -\partial_i\partial_j\psi(\theta)$ does not depend on $x$, so $\Gamma^{(1)}_{ij,k} = -\partial_i\partial_j\psi\,E[\partial_k\ell] = 0$. $\theta$ is an $e$-affine coordinate system.

> [!question]- ig-ac-mix-flat | Why is a mixture family $m$-flat?
> For $p = C + \theta^iF_i$, $\partial_i\ell = F_i/p$ and $\partial_i\partial_j\ell = -F_iF_j/p^2$, so $\partial_i\partial_j\ell + \partial_i\ell\,\partial_j\ell = 0$ and $\Gamma^{(-1)} = 0$ in the mixture parameters.

> [!question]- ig-ac-psi | In an exponential family, how are $g_{ij}$ and $T_{ijk}$ obtained from $\psi$?
> $g_{ij} = \partial_i\partial_j\psi(\theta)$ and $T_{ijk} = \partial_i\partial_j\partial_k\psi(\theta)$ in natural parameters: $\psi$ is the cumulant generating function.

> [!question]- ig-ac-normal-natural | Write $N(\mu, \sigma^2)$ as an exponential family.
> $F = (x, x^2)$, $\theta = (\mu/\sigma^2, -1/(2\sigma^2))$, $C = 0$, $\psi = -(\theta^1)^2/(4\theta^2) + \frac12\log(-\pi/\theta^2) = \mu^2/(2\sigma^2) + \log(\sqrt{2\pi}\sigma)$.

> [!question]- ig-ac-theorem-2-5 | State Theorem 2.5 and apply it to $\{N(\mu, 1)\}$ and $\{N(\mu, \mu^2)\}$.
> A submanifold of an exponential family is an exponential family iff it is $e$-autoparallel. $\{N(\mu, 1)\}$ is the line $\theta^2 = -1/2$, so yes; $\{N(\mu, \mu^2)\}$ is the parabola $\theta^2 = -(\theta^1)^2/2$, a curved exponential family.

> [!question]- ig-ac-not-metric | Show with the normal family that $\nabla^{(1)}$ is not metric but the pair $(\nabla^{(1)}, \nabla^{(-1)})$ satisfies a metric-like identity.
> $\partial_\sigma g_{\mu\mu} = -2/\sigma^3$, but $2\Gamma^{(1)}_{\sigma\mu,\mu} = -4/\sigma^3$. Mixing, $\Gamma^{(1)}_{\sigma\mu,\mu} + \Gamma^{(-1)}_{\sigma\mu,\mu} = -2/\sigma^3 + 0$ matches: duality.

> [!question]- ig-ac-location | Why is a location family $\{q(x - \mu)\}$ flat for every $\alpha$?
> In 1 dimension every connection is flat; the $k$-dimensional version is a product of 1-dimensional location models, so $\mu$ is affine for every $\alpha$ and the Fisher metric is constant (Euclidean). If $q$ is even, $T = 0$ and all $\alpha$-connections coincide.

## Where it leads

- [Chentsov's Theorem](04-Chentsovs-Theorem-and-Some-Historical-Remarks.md): the $\alpha$-connections are the only invariant connections.
- [The Geometry of P(X)](05-The-Geometry-of-P-of-X.md): $e$- and $m$-connections as the affine structures of $\log p$ and $p$.
- [Alpha-Affine Manifolds and Alpha-Families](06-Alpha-Affine-Manifolds-and-Alpha-Families.md) generalises exponential and mixture families to every $\alpha$.
- Code: [ch2_examples.py](code/ch2_examples.py) computes the normal-family table symbolically and checks (2.27) and Theorem 2.3.

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 2.3.
- Shun-ichi Amari, *Information Geometry and Its Applications*, Springer 2016, chapters 2 (exponential and mixture families) and 6 (dual connections, $\alpha$-geometry).
- Bradley Efron, "Defining the curvature of a statistical problem (with applications to second order efficiency)", *Annals of Statistics* 3(6) (1975), with A. P. Dawid's discussion introducing the $e$- and $m$-connections.
