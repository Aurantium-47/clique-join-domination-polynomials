# Stronger four-blade statement

This supplement proves concavity of the normalized coefficient sequence on the upper half for exactly four blades, a property stronger than unimodality. Its mathematical proof has a separate independent AI-review PASS in `independent_review.md`; the dated research-draft proof is preserved without alterations. This review was performed by AI, not by a human reviewer.

It is a special-case strengthening within the same original question, not a separately counted solved problem. Some four-blade unimodality cases were known before this work; see the review's prior-art qualification and the parent folder's `SOURCE_AND_SCOPE.md`.

To reproduce the exact checks:

```sh
python3 verify_four_blades.py > reproduced.json
cmp reproduced.json verification_output.json
```

The verifier checks 118,574 tuples through order 50, including 2,345,394 normalized-concavity inequalities. It also records a five-blade obstruction to extending this stronger normalized property, not a counterexample to unimodality.
