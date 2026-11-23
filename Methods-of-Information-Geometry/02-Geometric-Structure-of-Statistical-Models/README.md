---
type: moc
tier: core
status: solid
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) ch 2]
---

# Chapter 2: The Geometric Structure of Statistical Models

A statistical model is a manifold whose points are probability distributions, and that extra structure picks out a metric and a family of connections.
The Fisher metric measures how distinguishable nearby distributions are; the $\alpha$-connections, with the exponential ($\alpha = 1$) and mixture ($\alpha = -1$) connections at the ends, make exponential and mixture families flat.
Chentsov's theorem says these are the only structures invariant under sufficient statistics, and the geometry of $\mathcal{P}(\mathcal{X})$ shows the $e$- and $m$-connections preserving the metric only as a pair, which chapter 3 develops as duality.

6 sections, about 22.5 study hours.

| # | Section | Book | Pages | Hours | Cards |
| ---: | :--- | :--- | :--- | ---: | ---: |
| 01 | [Statistical Models](01-Statistical-Models.md) | 2.1 | 25-28 | 2 | 7 |
| 02 | [The Fisher Metric](02-The-Fisher-Metric.md) | 2.2 | 28-32 | 4 | 10 |
| 03 | [The Alpha-Connection](03-The-Alpha-Connection.md) | 2.3 | 32-36 | 5 | 10 |
| 04 | [Chentsov's Theorem and Some Historical Remarks](04-Chentsovs-Theorem-and-Some-Historical-Remarks.md) | 2.4 | 36-40 | 2.5 | 7 |
| 05 | [The Geometry of P(X)](05-The-Geometry-of-P-of-X.md) | 2.5 | 40-45 | 5 | 10 |
| 06 | [Alpha-Affine Manifolds and Alpha-Families](06-Alpha-Affine-Manifolds-and-Alpha-Families.md) | 2.6 | 45-50 | 4 | 10 |

## Running examples

- The normal family $N(\mu, \sigma^2)$: Fisher metric $\text{diag}(1/\sigma^2, 2/\sigma^2)$, natural parameters $(\mu/\sigma^2, -1/(2\sigma^2))$, and a full table of $e$-, $m$- and Levi-Civita coefficients in $(\mu, \sigma)$.
- The Bernoulli family: $g = 1/(p(1 - p))$, $m$-affine in $p$ and $e$-affine in the log-odds.
- $\mathcal{P}(\mathcal{X})$ on three points, $p = (0.5, 0.3, 0.2)$ and $q = (0.2, 0.3, 0.5)$: representations, parallel translation, the variance theorem, Fisher-Rao distance and $\alpha$-midpoints.

## Code

[code/ch2_examples.py](code/ch2_examples.py) computes and asserts every number quoted in this chapter's notes (Fisher matrices by three formulas, information loss, $\alpha$-connection coefficients, $e$/$m$ parallel translation, Jeffreys normalisers, denormalised connections).
Run it with `python3 code/ch2_examples.py`; it needs numpy, scipy and sympy and takes a few minutes because of the symbolic Gaussian integrals.
