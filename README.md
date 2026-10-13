# Domination polynomials of clique joins

Aurantium · v0.1.0 · 14 October 2026

For every r,a,b>=1, the domination polynomial of `K_r join (K_a disjoint-union K_b)` is ultra-log-concave of order N=r+a+b, hence log-concave and unimodal. The full proof treats the actual u_0=0 separately, includes all binomial-truncation cases and proves the required normalized inequalities at every index.

With three blades, ordinary log-concavity can fail. The 17-vertex graph `K_1 join (K_4 disjoint-union K_5 disjoint-union K_7)` has `(d_1,d_2,d_3)=(1,16,260)`, so `d_2^2-d_1*d_3=-4`. This particular polynomial remains unimodal. Allowing equal blade sizes, `K_1 join (K_q disjoint-union K_q disjoint-union K_q)` fails log-concavity for every integer q>=5.

- [Complete manuscript](paper/proof.pdf) and [standalone TeX](paper/proof.tex)
- [Exact scope](SCOPE.md), [reference and source discrepancy](REFERENCES.md)
- [Reproducibility and historical checks](REPRODUCIBILITY.md), [rights](RIGHTS.md)

The source is Rather's open question following Theorem 2.16, not an affirmative conjecture that all these properties hold. The counting formula is proved directly from the graph definition and agrees with that theorem. The extra term printed in Corollary 2.17 is not used; no author-issued correction is asserted.

The written proofs are independent of finite experiments. This preparation ran no mathematical program or old suite and bundles no unnecessary code. Existing checks are identified as historical in REPRODUCIBILITY.md. The note does not solve general t>=3 unimodality or zero-location questions, and claims neither a smallest counterexample nor first discovery or worldwide priority.

Prepared with AI assistance; no independent human peer review or proof-assistant certification is asserted. Third-party papers are linked, not bundled. WHITELIST.txt gives the payload, and MANIFEST.json lists hashes excluding itself.
