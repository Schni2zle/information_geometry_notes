---
type: moc
tier: core
status: solid
sources: [Amari and Nagaoka - Methods of Information Geometry (AMS and OUP 2000) ch 1]
---

# Chapter 1: Elementary Differential Geometry

The differential geometry needed for the rest of the book: manifolds, tangent spaces, tensors, metrics, connections, curvature and submanifolds.
The book covers only the local theory, assumes global coordinate systems throughout, and treats connections through infinitesimal parallel translation instead of fibre bundles.
The two ideas to carry forward are that a metric and a connection are independent structures, and that the Levi-Civita connection is only one choice among many.

10 sections, about 24.5 study hours.

| # | Section | Book | Pages | Hours | Cards |
| ---: | :--- | :--- | :--- | ---: | ---: |
| 01 | [Differentiable Manifolds](01-Differentiable-Manifolds.md) | 1.1 | 1-4 | 2 | 8 |
| 02 | [Tangent Vectors and Tangent Spaces](02-Tangent-Vectors-and-Tangent-Spaces.md) | 1.2 | 5-7 | 2 | 8 |
| 03 | [Vector Fields and Tensor Fields](03-Vector-Fields-and-Tensor-Fields.md) | 1.3 | 8-9 | 2 | 7 |
| 04 | [Submanifolds](04-Submanifolds.md) | 1.4 | 10-11 | 1.5 | 6 |
| 05 | [Riemannian Metrics](05-Riemannian-Metrics.md) | 1.5 | 11-12 | 2 | 8 |
| 06 | [Affine Connections and Covariant Derivatives](06-Affine-Connections-and-Covariant-Derivatives.md) | 1.6 | 13-17 | 4 | 9 |
| 07 | [Flatness](07-Flatness.md) | 1.7 | 17-19 | 3 | 9 |
| 08 | [Autoparallel Submanifolds](08-Autoparallel-Submanifolds.md) | 1.8 | 19-22 | 2.5 | 8 |
| 09 | [Projection of Connections and Embedding Curvature](09-Projection-of-Connections-and-Embedding-Curvature.md) | 1.9 | 22-23 | 2.5 | 7 |
| 10 | [Riemannian Connection](10-Riemannian-Connection.md) | 1.10 | 23-24 | 3 | 8 |

## Running examples

Three examples recur through the chapter so each new notion can be checked on something familiar:

- the plane in polar coordinates: flat, but with non-zero connection coefficients $\Gamma^r_{\theta\theta} = -r$, $\Gamma^\theta_{r\theta} = 1/r$;
- the unit sphere: $g = \text{diag}(1, \sin^2\theta)$, curvature 1, path-dependent parallel translation;
- the normal family $N(\mu, \sigma^2)$ with the Fisher metric $(d\mu^2 + 2d\sigma^2)/\sigma^2$: a hyperbolic plane of curvature $-1/2$, which chapter 2 derives.

## Code

[code/ch1_examples.py](code/ch1_examples.py) computes and asserts every number quoted in this chapter's notes (Jacobians, Christoffel symbols, curvature and torsion tensors, parallel translation by numerical integration).
Run it with `python3 code/ch1_examples.py`; it needs numpy, scipy and sympy.
