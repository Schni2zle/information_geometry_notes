---
type: concept
tier: advanced
status: solid
section: 2.4
pages: 36-40
prereqs: [the-fisher-metric, the-alpha-connection]
est_hours: 2.5
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) section 2.4, Chentsov - Statistical Decision Rules and Optimal Inference (AMS Translations 1982), Campbell - An Extended Cencov Characterization of the Information Metric (Proc AMS 1986), Ay Jost Le and Schwachhofer - Information Geometry (Springer 2017) ch 2 and 5]
---

# Chentsov's Theorem and Some Historical Remarks

## TL;DR

- A manifold carries infinitely many metrics and connections; the Fisher metric and $\alpha$-connections are distinguished by an invariance requirement that only makes sense because points are probability distributions.
- If $F$ is a sufficient statistic for $S$, then $S$ and the induced model $S_F$ have the same $\partial_i\log p$, hence the same $g_{ij}$ and $\Gamma^{(\alpha)}_{ij,k}$: the Fisher metric and $\alpha$-connections are invariant under sufficient statistics.
- Chentsov's theorem (Theorem 2.6): on the families $\mathcal{P}_n$ of distributions on finite sets, any family of metrics and connections invariant under sufficient statistics must be $c \times$ Fisher metric and an $\alpha$-connection, with the same $c > 0$ and $\alpha$ for all $n$.
- For infinite $\mathcal{X}$, approximate by finite partitions; requiring continuity in the limit again leads to the Fisher metric and $\alpha$-connections.
- History: Rao (1945) metric, Efron (1975) statistical curvature, Dawid (1975) $e$/$m$-connections, Chentsov (1972) invariance and $\alpha$-connections, Amari (1980) $\alpha$-connections and the $e$/$m$ pair, Nagaoka and Amari (1982) duality and dually flat spaces.

## Learning objectives

- State the invariance property of the Fisher metric and the $\alpha$-connections under sufficient statistics.
- State Chentsov's theorem and explain what it rules out.
- Explain the partition argument for infinite sample spaces.
- Place the main contributions to information geometry in historical order.

## Core concepts

### Why the Fisher metric is special

Sections 1.5 and 1.6 showed a manifold admits infinitely many Riemannian metrics and affine connections, and statistical manifolds are no exception.
A statistical model, however, has structure beyond being a manifold: each point is a probability distribution.
Taking this into account, there are natural structural conditions that the Fisher metric and the $\alpha$-connections uniquely satisfy.

### Invariance under sufficient statistics

Let $S = \{p(x; \xi)\}$ be a model on $\mathcal{X}$ and $F : \mathcal{X} \to \mathcal{Y}$, inducing $S_F = \{q(y; \xi)\}$ on $\mathcal{Y}$.
If $F$ is sufficient for $S$, then by (2.16) $\partial_i\log p(x; \xi) = \partial_i\log q(F(x); \xi)$, so $g_{ij}$ and $\Gamma^{(\alpha)}_{ij,k}$ computed on $S$ and on $S_F$ coincide.
This is the invariance of the Fisher metric and the $\alpha$-connection with respect to $F$.
With $\lambda : S \to S_F$, $\lambda(p_\xi) = q_\xi$, and $\lambda_* : \mathcal{T}(S) \to \mathcal{T}(S_F)$, $(\lambda_*(X))_{\lambda(p)} = (d\lambda)_p(X_p)$, the invariance reads

$$
\langle X, Y\rangle_p = \langle\lambda_*(X), \lambda_*(Y)\rangle'_{\lambda(p)}, \qquad \lambda_*(\nabla^{(\alpha)}_XY) = \nabla'^{(\alpha)}_{\lambda_*(X)}\lambda_*(Y)
$$

for all $X, Y \in \mathcal{T}(S)$, where primes denote the structures on $S_F$: $\lambda$ is an isometry that also preserves the connections.
This invariance is central to understanding how statistics and probability theory relate to the geometry of models.

### Chentsov's theorem

Let $\mathcal{X}_n = \{0, 1, \dots, n\}$ and $\mathcal{P}_n = \mathcal{P}(\mathcal{X}_n)$ for $n = 1, 2, \dots$
Suppose a sequence $\{(g_n, \nabla_n)\}_{n=1}^\infty$ is given, where $g_n$ is a Riemannian metric and $\nabla_n$ an affine connection on $\mathcal{P}_n$.
For a model $S \subset \mathcal{P}_n$ and a surjection $F : \mathcal{X}_n \to \mathcal{X}_m$ ($n \ge m$), the structures $(g_n, \nabla_n)$ and $(g_m, \nabla_m)$ induce metrics and connections on $S \subset \mathcal{P}_n$ and $S_F \subset \mathcal{P}_m$ by restriction and projection (sections 1.5 and 1.9).

**Theorem 2.6 (Chentsov).** Assume $\{(g_n, \nabla_n)\}$ is invariant with respect to sufficient statistics: for all $n, m$, $S \subset \mathcal{P}_n$ and $F : \mathcal{X}_n \to \mathcal{X}_m$ sufficient for $S$, the induced metrics and connections on $S$ and $S_F$ are invariant. Then there exist $c > 0$ and $\alpha \in \mathbb{R}$ such that for all $n$, $g_n$ is the Fisher metric on $\mathcal{P}_n$ scaled by $c$, and $\nabla_n$ is the $\alpha$-connection on $\mathcal{P}_n$.

(The book omits the proof; Chentsov's original formulation uses Markov morphisms between simplices.)
So on finite sets, invariance under sufficient statistics characterises the Fisher metric up to a constant and the $\alpha$-connections, which are then the only metric and connections that respect the statistical meaning of the points.

### Infinite sample spaces

Extending the theorem to infinite $\mathcal{X}$ is not easy: its formulation and proof rely on finiteness.
Heuristically, partition $\mathcal{X}$ into finitely many regions $\Delta = \{\delta_1, \dots, \delta_n\}$ ($\delta_i \cap \delta_j = \emptyset$, $\bigcup\delta_i = \mathcal{X}$) and let

$$
p_\Delta(\delta_i; \xi) = \int_{\delta_i}p(x; \xi)\,dx.
$$

$S_\Delta = \{p_\Delta(\delta_i; \xi)\}$ is a model on the finite set $\Delta$, so Chentsov's theorem fixes its metric and connections as Fisher and $\alpha$.
$S$ is the limit of $S_\Delta$ as the partition is refined, and if the structures should be continuous under such limits, they must be the limits of the Fisher metric and $\alpha$-connections on $S_\Delta$, which under regularity conditions are the Fisher metric and $\alpha$-connections on $S$.

### Historical remarks

- **Rao (1945)** pointed out that the Fisher information matrix defines a Riemannian metric on a model and stressed analysing model structure through Riemannian geometry; several follow-up attempts produced few results that fed back into statistics.
- **Efron (1975)** introduced the statistical curvature of 1-parameter models and showed it governs higher-order asymptotic estimation theory.
- **Dawid (1975)** introduced a connection on the space $\mathcal{P}$ of all positive distributions, showed statistical curvature is the embedding curvature with respect to it (the $e$-connection), and noted other connections are possible, giving the Levi-Civita (0-) connection and the $m$-connection as examples. $\mathcal{P}$ is infinite-dimensional and hard to treat rigorously.
- **Amari (1980)** reformulated Dawid's ideas by projecting onto finite-dimensional models, introduced the $\alpha$-connections, and made clear the importance of the $e$- and $m$-connections as a pair, leading to dual connections.
- **Nagaoka and Amari (1982)** introduced the duality of connections and the general theory of dually flat spaces, the mathematical foundation of $\alpha$-connections and a central part of information geometry.
- **Chentsov (1972)** had already introduced the $\alpha$-connections from the different perspective of invariance; the paper was in Russian, did not pursue the relation to curvature and estimation, and was not widely known internationally at first.

## Worked examples

### A sufficient statistic leaves $g$ and $T$ unchanged

Build a model on $\mathcal{X} = \{0, 1, 2, 3\}$ in two stages: first draw $y \in \{0, 1\}$ from Bernoulli($\xi$), then pick $x$ with $F(x) = x \bmod 2 = y$ using fixed probabilities that do not depend on $\xi$.
So $S_F = \{q(y; \xi)\}$ is Bernoulli, $q(1; \xi) = \xi$ and $q(0; \xi) = 1 - \xi$.
$S = \{p(x; \xi)\}$ has $p(x; \xi) = q(F(x); \xi)\,r(x)$, where $r(x)$ is the probability of $x$ given $F(x)$:

| $x$ | $F(x)$ | $r(x)$ | $p(x; \xi)$ | $\partial_\xi\log p(x; \xi)$ |
| ---: | ---: | ---: | :--- | :--- |
| 0 | 0 | 0.3 | $0.3(1 - \xi)$ | $-1/(1 - \xi)$ |
| 2 | 0 | 0.7 | $0.7(1 - \xi)$ | $-1/(1 - \xi)$ |
| 1 | 1 | 0.6 | $0.6\,\xi$ | $1/\xi$ |
| 3 | 1 | 0.4 | $0.4\,\xi$ | $1/\xi$ |

$F$ is sufficient by the factorisation (2.17), since $r$ does not involve $\xi$.
Taking logs, $\log r(x)$ drops out of the derivative, so the score of $p$ at $x$ is the Bernoulli score of $q$ at $F(x)$, which is (2.16).
At $\xi = 0.3$, both the 4-point model $S$ and the Bernoulli model $S_F$ have $g = 4.7619$ and $T = 9.0703$, so every $\alpha$-connection agrees too.

### Bernoulli trials and the number of successes

$n$ independent Bernoulli($\xi$) trials with $F$ = the number of successes is the standard sufficient statistic, and working it through makes each piece of the invariance statement concrete.
Write $w = \xi(1 - \xi)$.

> [!question]- ig-ch-binomial | For $n$ Bernoulli($\xi$) trials and $F(x)$ = the number of successes, identify $S$, $S_F$, $\lambda$ and $\lambda_*$, check that $F$ is sufficient, and show that $g$ and $\Gamma^{(\alpha)}$ agree on $S$ and $S_F$. What changes if $F$ is the first trial only?
> **Models.**
> $S$ lives on $\mathcal{X} = \{0, 1\}^n$ with $p(x; \xi) = \xi^{s(x)}(1 - \xi)^{n - s(x)}$, where $s(x) = x_1 + \dots + x_n$.
> $S_F$ lives on $\mathcal{Y} = \{0, \dots, n\}$ with $q(y; \xi) = \binom{n}{y}\xi^y(1 - \xi)^{n - y}$, because each of the $\binom{n}{y}$ sequences with $y$ successes has probability $\xi^y(1 - \xi)^{n - y}$.
> $\lambda$ sends Bernoulli-sequence($\xi$) to Binomial($n$, $\xi$); in the coordinate $\xi$ it is the identity, so $\lambda_*(\partial_\xi) = \partial'_\xi$.
>
> **Sufficiency.**
> $p(x; \xi) = q(F(x); \xi)\,r(x)$ with $r(x) = 1/\binom{n}{s(x)}$ free of $\xi$, so the factorisation (2.17) holds.
> Equivalently, given $s$, the sequence $x$ is uniform over the $\binom{n}{s}$ arrangements whatever $\xi$ is.
>
> **Scores agree (2.16).**
> The $\log\binom{n}{y}$ term has no $\xi$, so
>
> $$
> \partial_\xi\log p(x; \xi) = \frac{s - n\xi}{w} = \partial_\xi\log q(F(x); \xi).
> $$
>
> The score on $\mathcal{X}$ is the score on $\mathcal{Y}$ composed with $F$, which is $\lambda_*(\partial_\xi) = \partial'_\xi$ read through score functions.
>
> **Why the expectations agree.**
> For any function $h$, group the sum over $\mathcal{X}$ by the value of $F$:
>
> $$
> \sum_{x \in \mathcal{X}} p(x; \xi)\,h(s(x)) = \sum_{y=0}^{n}\sum_{x : s(x) = y} p(x; \xi)\,h(y) = \sum_{y=0}^{n} q(y; \xi)\,h(y).
> $$
>
> The first step only reorders the terms, and the second uses $q(y; \xi) = \sum_{x : s(x) = y} p(x; \xi)$, the definition of the distribution of $F$; normalisation is not used.
> This change of variables holds for every $F$; sufficiency is what makes the integrands of $g$ and $\Gamma^{(\alpha)}$ functions of $F(x)$, so they pass through unchanged.
> For $n = 2$ the sequences 01 and 10 have the same probability $w$ and the same score $(1 - 2\xi)/w$, and merge into the single count $y = 1$ with $q(1; \xi) = 2w$.
>
> **Fisher metric.**
> With $u = s - n\xi$, $E[u^2] = \text{Var}(s) = nw$, so $g = E[u^2]/w^2 = n/(\xi(1 - \xi))$.
> The Hessian form agrees: $-E[\partial_\xi^2\ell] = E[s/\xi^2 + (n - s)/(1 - \xi)^2] = n/\xi + n/(1 - \xi)$.
>
> **$\alpha$-connection.**
> Expanding around $n\xi$, $\partial_\xi^2\ell = -n/w - (1 - 2\xi)u/w^2$, and the binomial third central moment is $E[u^3] = nw(1 - 2\xi)$, so
>
> $$
> E[\partial_\xi^2\ell\,\partial_\xi\ell] = -\frac{n(1 - 2\xi)}{w^2}, \qquad T = \frac{n(1 - 2\xi)}{w^2}, \qquad \Gamma^{(\alpha)}_{\xi\xi,\xi} = -\frac{1 + \alpha}{2}\cdot\frac{n(1 - 2\xi)}{w^2}.
> $$
>
> At $n = 10$, $\xi = 0.3$, summing over all $2^{10}$ sequences and over the 11 counts gives identical values:
>
> | | $S$ (sequences) | $S_F$ (counts) |
> | :--- | ---: | ---: |
> | $g$ | 47.619 | 47.619 |
> | $T$ | 90.703 | 90.703 |
> | $\Gamma^{(1)}$ | $-90.703$ | $-90.703$ |
> | $\Gamma^{(0)}$ | $-45.351$ | $-45.351$ |
> | $\Gamma^{(-1)}$ | 0 | 0 |
>
> $\Gamma^{(-1)} = 0$ because $\xi$ is $m$-affine, $2\Gamma^{(0)} = \partial_\xi g$ is the metric condition (1.66) in one dimension, and $n = 1$ recovers the Bernoulli values $g = 4.7619$, $T = 9.0703$.
>
> **First trial only.**
> The score of $S_F$ composed with $F$ is $(x_1 - \xi)/w$, not $(s - n\xi)/w$, so (2.16) fails.
> $\lambda_*(\partial_\xi) = \partial'_\xi$ still holds, but $g' = 1/w = 4.762$ against $g = 47.619$, so $\lambda$ shrinks lengths.
> The loss $g - g' = (n - 1)/w = 42.857$ equals $E[\text{Var}(\partial_\xi\ell \mid F)] = \text{Var}(x_2 + \dots + x_n)/w^2$, the information in the discarded trials, as the information-loss formula (2.18) of Theorem 2.1 says.

### The Euclidean metric is not invariant

Treat the same two models as curves of probability vectors and use the squared Euclidean length of the velocity as a metric.
For $S_F$, the vector $(1 - \xi, \xi)$ has velocity $(-1, 1)$, so the metric is $1 + 1 = 2$.
For $S$, each component $r(x)(1 - \xi)$ or $r(x)\xi$ has derivative $\pm r(x)$, so the metric is $0.09 + 0.49 + 0.36 + 0.16 = 1.1$.
$2 \neq 1.1$, so the Euclidean metric on probability vectors depends on how outcomes are split, which Chentsov's invariance forbids.
The Fisher metric $\sum_x(\partial_\xi p(x; \xi))^2/p(x; \xi)$ divides each term by the probability: on $S$ it gives $(0.3 + 0.7)/(1 - \xi) + (0.6 + 0.4)/\xi = 1/(\xi(1 - \xi))$, the same as on $S_F$.

## Pitfalls

- Reading Chentsov's theorem as "the Fisher metric is the only metric"; it is unique up to the constant $c$, and only among families invariant under sufficient statistics (Markov morphisms).
- Forgetting the connection part; invariance does not single out one connection but the whole $\alpha$-family, with a free parameter $\alpha$.
- Applying the finite-set theorem directly to continuous models; the infinite case needs extra regularity or a limiting argument.
- Calling the $\alpha$-connections an invention of one author; Chentsov, Dawid and Amari arrived at them from invariance, curvature and higher-order asymptotics respectively.

## Review questions

> [!question]- ig-ch-invariance | Why are the Fisher metric and $\alpha$-connections invariant under a sufficient statistic $F$?
> By factorisation $p(x; \xi) = q(F(x); \xi)r(x)$, so $\partial_i\log p = \partial_i\log q(F(x); \xi)$. Both $g$ and $\Gamma^{(\alpha)}$ are expectations of products of these derivatives, so they are the same on $S$ and on $S_F$.

> [!question]- ig-ch-theorem | State Chentsov's theorem.
> If metrics $g_n$ and connections $\nabla_n$ on $\mathcal{P}_n = \mathcal{P}(\{0, \dots, n\})$ are invariant under sufficient statistics between all such models, then $g_n = c \cdot$ Fisher metric and $\nabla_n = \nabla^{(\alpha)}$ for one $c > 0$ and one $\alpha \in \mathbb{R}$, for all $n$.

> [!question]- ig-ch-infinite | How is Chentsov's result extended heuristically to infinite $\mathcal{X}$?
> Partition $\mathcal{X}$ into finitely many cells, so the coarse-grained model lives on a finite set where the theorem applies, then refine. Continuity of the structures under refinement forces the Fisher metric and $\alpha$-connections in the limit.

> [!question]- ig-ch-euclidean | Show with a concrete example that the Euclidean metric on probability vectors is not invariant under sufficient statistics.
> Bernoulli $(1 - \xi, \xi)$ gives $\sum_x(\partial_\xi p(x; \xi))^2 = 2$; splitting each outcome by fixed conditionals $(0.3, 0.7)$ and $(0.6, 0.4)$ gives $1.1$. The Fisher metric $\sum_x(\partial_\xi p(x; \xi))^2/p(x; \xi)$ gives $1/(\xi(1 - \xi))$ in both.

> [!question]- ig-ch-history | Who introduced the Fisher metric as a Riemannian metric, statistical curvature, the $e$-connection, and dually flat spaces?
> Rao (1945); Efron (1975); Dawid (1975, as the connection whose embedding curvature is Efron's curvature); Nagaoka and Amari (1982).

> [!question]- ig-ch-free-parameters | Which free parameters remain after imposing invariance, and what does each mean?
> The scale $c$ of the metric (a choice of units) and $\alpha$ for the connection. Different $\alpha$ give the one-parameter family linking the $m$- ($\alpha = -1$), Levi-Civita ($\alpha = 0$) and $e$- ($\alpha = 1$) connections.

## Where it leads

- [The Geometry of P(X)](05-The-Geometry-of-P-of-X.md) builds the Fisher metric and $e$/$m$-connections of $\mathcal{P}_n$ explicitly.
- Chapter 3 (dual connections) develops the Nagaoka-Amari duality mentioned in the history.
- Code: [ch2_examples.py](code/ch2_examples.py).

## Further reading

- Amari and Nagaoka, *Methods of Information Geometry*, section 2.4.
- N. N. Chentsov (Cencov), *Statistical Decision Rules and Optimal Inference*, Translations of Mathematical Monographs 53, AMS 1982 (Russian original 1972).
- L. L. Campbell, "An extended Cencov characterization of the information metric", *Proceedings of the AMS* 98(1) (1986).
- Nihat Ay, Jurgen Jost, Hong Van Le and Lorenz Schwachhofer, *Information Geometry*, Springer 2017, which proves Chentsov-type theorems for general sample spaces.
