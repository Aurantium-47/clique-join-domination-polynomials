# Proof and execution scope

The parameter-wide results are fully written counting and algebraic proofs. No computational certificate is needed: partition dominating sets by whether they meet the central clique, take coefficients, prove the exact second-difference formula with zero conventions, handle u_0=0 separately, and apply the normalized inequalities. The three-blade failures follow from direct counts of sets of sizes 1,2,3 and the displayed polynomial inequality in q.

No mathematical program, enumeration, old author suite or new entry point was run in preparing this note. No program is bundled merely to repeat a closed check.

## Historical finite checks

The retained execution documentation for 13 October 2026 identifies Python 3.8.3. Two relevant successful receipts record exit 0 and empty stderr:

| Check | Actual recorded finite range | Recorded external wall time | Recorded child peak working set |
|---|---|---|---|
| Two-blade ULC | r,a,b each in 1,...,12: 1728 ordered triples, 63936 second-difference equalities and 31968 ULC inequalities, using exact integers/Fraction | 0.6346819000000001 s | 15429632 bytes |
| Direct graph enumeration | All vertex subsets of the 17-vertex 4/5/7 graph and 16-vertex 5/5/5 graph, plus full coefficients for four small two-blade graphs | 0.250864 s | 15372288 bytes |

The full recorded coefficient vectors have modes 9 and 8 for the two three-blade examples. The 17-vertex vector is transcribed in the manuscript and makes its unimodality explicit. The counterexample proof only needs its directly counted first three coefficients.

The first attempt at the graph check exited 1 because the old interpreter did not provide `int.bit_count()`. Its failure was retained; the independently written check replaced that call with `bin(mask).count('1')` and subsequently passed. This was an environment-compatibility repair, not a mathematical counterexample, and it did not modify the author's original code. The previous failure is not hidden behind a claim of first-attempt success.

The independent 1728-triple check is not a rerun of the author's different 1680-triple table or the larger 12008-parameter graph scan. Those full tables are not claimed verified by this manuscript preparation. Historical results check their finite ranges; the written argument proves the all-positive-parameter theorem. Process memory observations did not measure all parent/tool/PDF processes and are not performance promises.

The underlying historical scripts, receipts and failures are preserved separately, but the unrelated multi-topic suite is not distributed here. No new portable mathematical entry is claimed to have run.

## Rebuilding the PDF

`paper/proof.tex` is standalone. With its standard LaTeX packages installed, run `pdflatex proof.tex` twice from `paper/` for references. No figures, external bibliography program, mathematical calculation or third-party PDF is required. A rebuild can change PDF timestamps/font encoding; MANIFEST.json identifies the supplied bytes. Compilation and visual checks do not constitute a new mathematical review.
