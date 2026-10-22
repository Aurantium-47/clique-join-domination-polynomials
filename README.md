# Domination polynomials of clique joins

**Aurantium · Updated 22 October 2026**

For every positive core order r and every nonempty finite list of positive blade orders a₁,…,aₜ, the domination polynomial of **Kᵣ ∨ (Kₐ₁ ∪ ⋯ ∪ Kₐₜ) is unimodal**.

The [complete computer-assisted proof](all-blades/all_blades_proof.md) is analytic for N≥23 and uses an exhaustive exact certificate for all **14,464** core/blade tuples of order N≤22. An independent AI mathematical audit returned PASS. This is not human peer review or Lean certification.

## Original question and previous work

Bilal Ahmad Rather asked about the zeros, log-concavity and unimodality of this family immediately after Theorem 2.16, p. 286, in *On domination polynomials of some graphs*, **JCMCC 126 (2025), 279–289**, published online **24 June 2025** ([DOI](https://doi.org/10.61091/jcmcc126-19)). This is an unnumbered question, not an affirmative conjecture that all properties hold.

Burcroff–O’Brien (2021) already covered all three-blade cases and odd-order four-blade cases through upper-domination-number criteria. Zhang (2021) covered every graph with a universal vertex of order at least 8192. Omar (2026) supplied threshold-graph log-concavity and further sufficient criteria. The present result gives a **uniform whole-family answer to the unimodality part**, including the parameters not covered by those checked results. See [source dates and prior-art boundaries](all-blades/SOURCE_AND_SCOPE.md).

## Results and scope

- **All blades:** unimodality for all positive r,t,aᵢ. This is not the general domination-polynomial unimodality conjecture for arbitrary graphs.
- **Two blades, earlier result:** ultra-log-concavity of order N, hence log-concavity and unimodality, for all r,a,b≥1.
- **Three blades, earlier result:** ordinary log-concavity fails for the 17-vertex (r;a,b,c)=(1;4,5,7) example and for (1;q,q,q) with q≥5. These are not nonunimodality examples.
- **Four blades:** [stronger normalized-tail concavity](all-blades/four_blade_strengthening/four_blade_proof.md), retained within the same result group, not counted as a separate solution.

The zeros and limiting-zero questions remain open here. The erroneous extra term in printed Corollary 2.17 is not used. No smallest counterexample, first-discovery or worldwide-priority claim is made.

## Proof and verification

- [All-blade proof](all-blades/all_blades_proof.md), [exact certificate](all-blades/verification_all_blades.json), and [independent AI audit](all-blades/independent_all_blades_review.md)
- [Reproduction instructions](REPRODUCIBILITY.md) and [exact scope](SCOPE.md)
- Earlier two-/three-blade [manuscript PDF](paper/proof.pdf) and [TeX](paper/proof.tex), retained as the earlier version, not the all-blade proof
- [References](REFERENCES.md), [rights](RIGHTS.md), [file list](WHITELIST.txt), and [integrity manifest](MANIFEST.json)

## 中文摘要

Rather于2025年在JCMCC提出的问题包含零点、对数凹性与单峰性。本次证明其中的**全家族单峰性**：任意正整数核心大小、叶片数及叶片大小均成立。N≥23用解析证明，N≤22用14,464组参数的精确穷尽证书。已通过独立AI复核，但不是人工同行评审，也未完成Lean形式化。

原有两叶片超对数凹性、三叶片非对数凹反例保留；四叶片的更强结论属于同一成果组，不重复计数。已知特殊情形不作为新成果再次计算，零点问题亦不宣称解决。
