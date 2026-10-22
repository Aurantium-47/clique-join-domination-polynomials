# Exact mathematical scope

All graphs are finite, simple and undirected. The central clique has positive order r; each of the t≥1 blades is a nonempty clique. Distinct blades have no edges between them; every central vertex is adjacent to every blade vertex. Blade orders may coincide.

## Current all-blade theorem

For every such graph, the domination polynomial is unimodal. The proof is analytic for every N≥23 and exhaustive with exact integer certificates for N≤22, covering all 14,464 core/blade tuples in that range. The [complete proof](all-blades/all_blades_proof.md), [certificate](all-blades/verification_all_blades.json), and [independent AI audit](all-blades/independent_all_blades_review.md) establish this scope. The stronger four-blade normalized-tail statement is supplementary within this same result group.

## Earlier structural results

For exactly two blades, all r,a,b≥1 satisfy N-order ultra-log-concavity: uₖ=dₖ/binom(N,k) is log-concave with no internal zeros. The actual u₀=0 is handled separately, as are all binomial truncations.

For r=1 and blade orders 4,5,7, ordinary log-concavity fails at k=2. The polynomial is nevertheless unimodal. The equal-blade family (1;q,q,q), q≥5, also fails log-concavity, not unimodality. No smallest counterexample is asserted. The retained manuscript in paper/ proves these earlier results and is not the all-blade update.

## Boundaries

Rather's question after Theorem 2.16 also asks about zeros and their limits; those parts are not resolved here. Universal log-concavity is false. General domination-polynomial unimodality for arbitrary graphs is not established. The direct counting formula avoids the extra term in printed Corollary 2.17 without purporting to amend the author's publication.

The current proof passed independent AI mathematical review, not independent human peer review. No Lean certification or worldwide-priority conclusion is claimed. Earlier known special cases and the supplementary four-blade result are not separate new solved-problem counts. See [source and prior-art boundaries](all-blades/SOURCE_AND_SCOPE.md).
