---
type: moc
tier: core
status: draft
sources: [Amari and Nagaoka - Methods of Information Geometry (Translations of Mathematical Monographs 191 AMS and OUP 2000)]
---

# Methods of Information Geometry

Study notes on Shun-ichi Amari and Hiroshi Nagaoka, *Methods of Information Geometry* (AMS and Oxford University Press, 2000; translated by Daishi Harada), one note per numbered section, in folders by chapter.
The book itself is not included; section numbers, page numbers and equation numbers refer to the 2000 AMS edition.

| Chapter | Sections | Status |
| :--- | ---: | :--- |
| [1. Elementary Differential Geometry](01-Elementary-Differential-Geometry/README.md) | 10 | written |
| [2. The Geometric Structure of Statistical Models](02-Geometric-Structure-of-Statistical-Models/README.md) | 6 | written |
| 3. Dual Connections | 8 | not started |
| 4. Statistical Inference and Differential Geometry | 8 | not started |
| 5. The Geometry of Time Series and Linear Systems | 4 | not started |
| 6. Multiterminal Information Theory and Statistical Inference | 4 | not started |
| 7. Information Geometry for Quantum Systems | 4 | not started |
| 8. Miscellaneous Topics | 4 | not started |

## Note format

The notes follow the conventions of The-Quant-Prep (`00-Start-Here/Note-Conventions.md`), adapted for a textbook:

- Frontmatter: `type`, `tier`, `status`, the book `section` and `pages`, `prereqs` (note ids, the file name without its number prefix, lower-cased), `est_hours` and `sources`.
- Sections in order: `## TL;DR`, `## Learning objectives`, `## Core concepts` (the book's content with its equation numbers, so you can cross-reference the scan), `## Worked examples`, `## Pitfalls`, `## Review questions`, `## Where it leads`, `## Further reading`.
- Review questions are collapsible Obsidian callouts, `> [!question]- <id> | <prompt>`, with ids prefixed `ig-` and unique across the folder.
- Every number in a worked example or card is computed and asserted by the chapter's `code/chN_examples.py`.
- One sentence per line, no em dashes, relative Markdown links.

Index conventions are the book's: $\nabla_{\partial_i}\partial_j = \Gamma^k_{ij}\partial_k$, $\Gamma_{ij,k} = \langle\nabla_{\partial_i}\partial_j, \partial_k\rangle$, $R(\partial_i, \partial_j)\partial_k = R^\ell_{ijk}\partial_\ell$, $\ell = \log p$.
