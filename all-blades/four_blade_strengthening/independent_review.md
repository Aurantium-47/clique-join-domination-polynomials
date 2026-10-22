# Independent AI mathematical review of the four-blade theorem

Review date: 22 October 2026. Reviewer: an independently tasked AI, not a human referee. This review is not external peer review, a publication, or a priority certificate.

## Independent AI-review verdict

The proof of upper-half normalized concavity for every positive integer tuple (r,a,b,c,d) is correct as written. No gap was found in the counting, relation multiplicities, small cases, or deduction of unimodality. Its scope is all four-blade graphs, not arbitrary numbers of blades. Literature attribution needs the qualifications below.

## Mathematical audit

1. A set dominates precisely when it meets the core or every blade. The two summands of the displayed generating function count disjoint classes.
2. Sampling ordered (S,x,y) uniformly does make each augmented set uniform in its own layer. The second-difference identity is exact. Monotonicity gives Z in {-1,0,1}.
3. A positive triple has no selected core vertex and misses exactly the two distinct blades containing x and y. The classification is both necessary and sufficient.
4. Q and its coordinate reversals are disjoint subsets of the negative triples, since one coordinate is central and the other is noncentral. Thus 2|Q| is a legitimate lower bound with no overcounting.
5. For a fixed positive triple, deleting distinct removable z gives distinct T, and choosing distinct u changes the recorded coordinate. Therefore its relation degree really is r times the number of removable vertices, without hidden multiplicity.
6. The inverse description is exact: x must be the unique T-vertex in a met blade X, and z must be outside T in one of the other two met blades. Conversely every such choice yields a valid positive predecessor, and z is removable because those two blade intersections remain nonempty after its deletion. The exact number for a fixed X is N-r-|X|-|Y|-j+1.
7. For j>=4, at most two of the three met blades of T can be singletons. A positive S has at most two nonremovable vertices. The bounds are therefore r(j-2) below and 2(N-r-j-1) above. If P is nonempty, N-r-j-1>=1, so the comparison of these nonnegative bounds is legitimate. The algebra N-r-j-1<=j-r-1<=r(j-2) is correct; the second inequality is (r-1)(j-1)>=0.
8. For j=3, N<=6 and existence of P forces N=6,r=1. The two met blade intersections of S have sizes 1 and 2, so exactly two vertices are removable. A Q-set has three singleton intersections and at most three predecessors. Hence 2|P|<=3|Q| is correct. N=5 has no positive triples. There are no j<3 cases.
9. Concavity of the positive normalized tail implies its log-concavity by AM-GM. Multiplication by the positive log-concave binomial sequence gives log-concavity of the coefficient tail. The independent incidence inequality (N-k)d_k<=(k+1)d_(k+1) proves nondecrease through h=ceil(N/2), including the odd-order equality boundary. The two portions combine to a unimodal full sequence.
10. No external lemma is needed for this proof: the counting argument, AM-GM, binomial log-concavity, and elementary implication from positive log-concavity to unimodality suffice. The letters M are reused for the blade total and negative triples, a harmless notation issue worth cleaning up.

## Reproduction and independent tests

The originally supplied script completed without any failed assertion:

- 118,574 sorted four-blade parameter tuples with 5<=N<=50.
- 2,345,394 exact normalized-concavity inequalities.
- 142 direct ordered-triple configuration cases with N<=10.
- The five-blade obstruction r=1, blades (1,1,1,1,5), N=10, j=5 has exact normalized second difference 1/126>0; its domination sequence is still unimodal.

The reproduction is saved in review_four_blades_reproduction.json. The updated script, including its N=12 Omar example, was rerun successfully; its exact value was also checked independently below.

As a separate implementation independent of the polynomial formula, I constructed each graph via closed-neighborhood bitmasks and enumerated every subset for every sorted four-blade tuple with 5<=N<=13. All 672,160 subset evaluations across 162 graph instances reproduced the formula's coefficient vectors exactly.

These finite checks support and test implementation details, but the general theorem rests on the proof above.

## Prior-art exclusions and cautions

- All three-blade cases and all odd-order four-blade cases are already covered by Burcroff--O'Brien Corollary 6.3, since the upper domination number is the number of blades.
- Zhang's universal-vertex theorem covers all orders N>=8192. Consequently only even N<8192 can be new unimodality coverage from the four-blade theorem, and even within that bounded range other prior criteria cover many graphs.
- Burcroff--O'Brien Theorem 7.4 covers r>=log_2(N)-1; their Theorem 7.2 can do better. Their minimum-degree citation also applies when r+min(a_i)-1>=2 log_2(N).
- Threshold cases are already covered by Omar. Within this family, threshold graphs have at most one blade of size greater than one; two nontrivial blades contain an induced 2K_2.
- The original three Omar-failing witnesses all have N=10. Zhang reports that Beaton--Brown already computationally verified all universal-vertex graphs through order ten. Those witnesses establish only failure of Omar's sufficient criterion, not new coverage.
- The added witness r=1, blades (1,2,2,6), N=12 also cannot establish new coverage: q_7=617/792>=5/8, so Beaton--Brown's ratio criterion (Burcroff--O'Brien Lemma 7.1) proves a decreasing tail from index 7. The increasing initial segment through 6 then proves unimodality.
- A better illustrative witness against several checked sufficient criteria is r=1, blades (1,2,2,14), N=20. Omar's quantity is 233/646>1/11; the exact ratio tests fail at both central indices: q_10=210/323<10/11 and q_11=9317/12920<3/4. It is not threshold and fails the stated high-degree/universal-count conditions. The upper-domination theorem only gives decrease from index 12. This is a witness to the limits of checked criteria, not a proof of worldwide priority.

The safe contribution description is a self-contained four-blade normalized-concavity theorem and the resulting uniform four-blade unimodality proof, with its genuinely additional unimodality coverage restricted by existing results. Do not describe this as resolving Rather's arbitrary-blade question or count previously established three-blade, odd-order, or large-order cases again.

Sources: Rather (2025), https://combinatorialpress.com/article/jcmcc/volume%20126/on-domination-polynomials-of-some-graphs.pdf ; Burcroff--O'Brien, https://arxiv.org/html/2110.00709 ; Zhang, https://arxiv.org/html/2111.00641 ; Omar, https://arxiv.org/html/2601.14494v1 .

Further scope note: targeted searches for trivially perfect, quasi-threshold, cograph, generalized windmill, and complete split graph unimodality did not identify a theorem covering the whole present family. This negative search result is not exhaustive. A conservative candidate region is even 12<=N<=8190, r<log_2(N)-1, with at least two nontrivial blades, and not already certified by applicable ratio, degree, overlap, or other known subfamily results. It is an upper bound on possible historical novelty, not a classification of all previously open tuples.
