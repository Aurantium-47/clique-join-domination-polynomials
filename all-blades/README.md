# All-blade unimodality: verified extension package

Prepared 22 October 2026 for the existing [clique-join project](https://github.com/Aurantium-47/clique-join-domination-polynomials). Published as the all-blade extension in this existing project.

**Result:** domination polynomials of K_r joined to any disjoint union of nonempty cliques are unimodal, for every positive core order and arbitrary positive blade orders.

**Status:** complete computer-assisted proof, independently reviewed by AI with PASS. Analytic for N≥23; exhaustive exact proof certificate for N≤22. This was not human review; it is not yet formalized in Lean or externally peer reviewed.

Start with `all_blades_proof.md`, `SOURCE_AND_SCOPE.md`, and `independent_all_blades_review.md`. The root README summarizes this update; it is not a new project or an additional count for the four-blade strengthening.

## Reproduce

From this folder, run:

```sh
python3 verify_all_blades.py > reproduced.json
cmp reproduced.json verification_all_blades.json
python3 audit_all_blades_bounds.py
python3 review_all_blades_counts.py
```

The first command certifies 14,464 tuples through N=22 and 233 exact arithmetic cases. It also checks 274 graph instances by enumerating 148,700 vertex subsets. The supplemental bound audit checks 159,534 index cases. The independent AI review script audits actual graph-level incidence counts and identities: 412 graphs, 431,324 subsets, and 1,377 layer checks. Its reproduced stdout is `review_all_blades_counts.txt`.

## Package organization

- Main proof, exact verifiers/results, and independent AI review are at the top level.
- `audited_snapshot/all_blades_proof.md` is the exact proof revision fingerprinted in the independent AI report. The clean top-level copy changes only its pre-review status paragraphs.
- `four_blade_strengthening/` preserves the stronger four-blade theorem and its exact checks. It is supplementary, not an additional solved-problem count.
- `SHA256SUMS.txt` records every packaged file other than itself.

No exploratory search logs or unverified conjectures are part of this release package. The original question also asks about roots and log-concavity; the present full result concerns unimodality only.
