# Original question, provenance, and prior-art boundaries

## Original published question

Bilal Ahmad Rather, *On domination polynomials of some graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing **126** (2025), 279–289, DOI [10.61091/jcmcc126-19](https://doi.org/10.61091/jcmcc126-19).

The [publisher record](https://combinatorialpress.com/jcmcc-articles/volume-126/on-domination-polynomials-of-some-graphs/) gives receipt on **22 April 2025**, revision on **20 May 2025**, acceptance on **29 May 2025**, and online publication on **24 June 2025**. The relevant location is **Theorem 2.16 and the immediately following unnumbered question, printed page 286**, PDF page 8 of 11. [Original PDF](https://combinatorialpress.com/article/jcmcc/volume%20126/on-domination-polynomials-of-some-graphs.pdf).

The question asks:

> What can be said about the domination zeros and their limits, log-concave and unimodal property of D(G,x)?

Its family is K_{n_1} joined to the disjoint union of K_{n_2},...,K_{n_t}. Our notation uses r=n_1 and a_i=n_{i+1}; our blade count is therefore one less than the source's tuple length. The present theorem proves the **unimodality part** for the entire family. It does not answer the zeros/limiting-zero questions. The general log-concavity assertion is false, as the existing project already records.

The source asks a question; it does not state a named affirmative conjecture for this family. The erroneous extra term printed in Corollary 2.17 is not used.

## Existing project and the extension

Target existing project: [Aurantium-47/clique-join-domination-polynomials](https://github.com/Aurantium-47/clique-join-domination-polynomials).

Previously recorded results include two-blade ultra-log-concavity and three-blade failure of log-concavity (including a 17-vertex example that is still unimodal). Those are not new results of this package. This package upgrades the unimodality scope from special cases to **all positive r,t,a_i**. It is one whole-family result, not separate solved-problem credits for t=2, t=3, t=4, each order, or previously known large-order cases.

The four-blade normalized-concavity theorem is retained as a stronger supplementary statement, not as a second resolution of the original question.

## Checked earlier sufficient results

### Burcroff–O'Brien

Amanda Burcroff and Grace O'Brien, *Unimodality and monotonic portions of certain domination polynomials*, [arXiv:2110.00709](https://arxiv.org/abs/2110.00709), first submitted **2 October 2021**.

Their Corollary 6.3 already implies unimodality for upper domination number at most three in even order and at most four in odd order. In this clique-join family the upper domination number is t: minimal dominating sets are central singletons or one vertex from each blade. Thus all three-blade cases and all odd-order four-blade cases were already covered. Their universal-vertex, degree, and ratio criteria cover additional parameters. [Full text](https://arxiv.org/html/2110.00709).

### Zhang

Shengtong Zhang, *Domination polynomial is unimodal for large graphs with a universal vertex*, [arXiv:2111.00641](https://arxiv.org/abs/2111.00641), first submitted **1 November 2021**, version 2 dated **2 November 2021**.

Theorem 1.2 already covers every graph with a universal vertex and order N≥8192, hence every member of the present family in that range. The new proof is independent of that theorem and analytically covers N≥23, with exact exhaustive certification below 23. The general incidence viewpoint in Zhang's work motivated our sharper clique-specific bounds. [Full text](https://arxiv.org/html/2111.00641).

### Omar

Mohamed Omar, *New Perspectives On The Unimodality Of Domination Polynomials*, [arXiv:2601.14494](https://arxiv.org/abs/2601.14494), first submitted **20 January 2026**.

The paper proves threshold-graph log-concavity and gives an overlap-corrected sufficient unimodality criterion. In our family, at most one nontrivial blade yields a threshold graph; two nontrivial blades give an induced 2K_2. These sufficient results do not uniformly cover arbitrary blades. The separate four-blade audit records exact overlap and ratio tests; its N=20 witness (r;a_i)=(1;1,2,2,14) fails those checked central criteria. That witness demonstrates limitations of the checked tests, not an exhaustive novelty certificate. [Full text](https://arxiv.org/html/2601.14494v1).

## What the verification establishes

- Complete computer-assisted proof of whole-family unimodality, with independent AI mathematical PASS (not human review).
- All N≥23 handled analytically; all 14,464 parameter tuples through N=22 checked exactly.
- No assertion of full log-concavity or arbitrary-graph unimodality.
- No Lean formalization or external peer review is claimed. This repository publication is not a peer-reviewed journal publication.
- Priority against all literature is not mechanically certified; this file records the checked major overlaps rather than claiming exhaustive worldwide priority.
