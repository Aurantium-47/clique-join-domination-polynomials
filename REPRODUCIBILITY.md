# Proof and reproducibility

## All-blade unimodality

The proof combines a uniform analytic argument for N≥23 with an exhaustive exact certificate for N≤22. From all-blades/, use Python 3.10 or newer with its standard library:

```sh
python3 verify_all_blades.py > reproduced.json
cmp reproduced.json verification_all_blades.json
python3 audit_all_blades_bounds.py
python3 review_all_blades_counts.py
```

The first verifier certifies all 14,464 core/blade tuples through N=22 and 233 exact arithmetic cases, and checks 274 graph instances by enumerating 148,700 vertex subsets. The bound audit covers 159,534 index cases. The independent graph-level incidence check covers 412 graphs, 431,324 subsets and 1,377 layers. Results and independent reproduction records are included in all-blades/.

The [independent AI review](all-blades/independent_all_blades_review.md) fingerprints the exact reviewed proof in all-blades/audited_snapshot/. The clean top-level proof differs only in status wording; the report explains that distinction. Independent AI review is not human peer review or proof-assistant certification.

The stronger four-blade theorem and exact checks are in all-blades/four_blade_strengthening/. They are supplementary to the same project, not an additional resolved-question count.

## Earlier two-/three-blade results

The retained paper/proof.pdf and paper/proof.tex contain the earlier parameter-wide counting and algebraic proofs of two-blade ultra-log-concavity and three-blade log-concavity failures. These proofs do not rely on finite experiments. Historical exact checks covered r,a,b in 1,…,12 (1,728 ordered triples) and direct subset enumeration of the 17-vertex (4,5,7) and 16-vertex (5,5,5) examples. The historical evidence is not described as a new reproduction of unrelated suites.

To rebuild the earlier manuscript, run pdflatex proof.tex twice from paper/. No third-party PDF, external bibliography processor or figures are needed. A PDF rebuild may change metadata; MANIFEST.json identifies the published bytes.

## Integrity

MANIFEST.json records SHA-256 hashes for the repository payload, excluding itself. all-blades/SHA256SUMS.txt records hashes inside that extension directory, excluding itself. Hash validation establishes byte integrity, not mathematical truth.
