# Independent AI review: arbitrary numbers of clique blades

Review date: 22 October 2026. Reviewer: an independently tasked AI, not a human referee. This report is not external peer review.

## Verdict

**Independent AI-review verdict: PASS as a complete computer-assisted mathematical proof.** The theorem establishes unimodality for every positive integer r, every positive blade count t, and every positive blade-size tuple. The proof is analytic for all N>=23 and exhaustively certified with exact arithmetic for 2<=N<=22. No circular use of unimodality, missing parameter regime, parity gap, or counting defect was found.

This verdict is distinct from priority review. It does not certify worldwide novelty or publication status. The earlier four-blade AI-review PASS is retained separately: that result proves a stronger normalized upper-tail concavity statement, while the present proof establishes ordinary concavity only in an appropriate central interval and decrease beyond it. It does not claim global log-concavity or domination-polynomial unimodality for arbitrary graphs.

## Detailed mathematical audit

### First differences

The repair count H_k and incidence identity (2) are exact. Nondominating sets avoid every core vertex, and the repair count is r+a_i when exactly blade i is missed and r otherwise. The events of missing exactly one specified blade are disjoint, which justifies the crucial alpha contribution being alpha rather than alpha times the number of blades.

Alpha is explicitly a nonnegative integer. For integer a>alpha, the ratio of consecutive values of (a-alpha)/(a*2^a) is strictly below one; hence the cutoff bound is valid. The minimum defining F exists because F_alpha(u)>=alpha, and F is nondecreasing as the minimum of nondecreasing functions.

For k>=ceil(N/2), the blade-avoidance binomial ratio is at most 2^(-a). The convention for zero binomial coefficients and the separate case k>A prevent any illegitimate conditional probability or negative-factor product.

The arbitrary-core reduction is correct: C(N-r,k)/C(N-1,k)<=2^(-(r-1)), r<=2^(r-1), F(N-r)<=F(N-1), and F is nonnegative. These inequalities indeed give H_k<=(1+F(N-1))C(N-1,k). The fixed-core lower bound for d_k and the positive factor 2k+1-N then prove strict decrease under condition (4). Both factors of (2k+1-N)*k/(N-k) are positive and increasing on the relevant interval.

### Second differences

The positive-triple classification is exact. The key enlargement is legitimate: for each fixed i, sets missing exactly {i,j} are disjoint as j varies. Thus replacing 2a_i*a_j by a_i^2+a_j^2 does not introduce an extra multiplicity when bounding their union by all sets avoiding blade i. This proves T_k<=sum_i a_i^2 C(A-a_i,k), and a_i*2^(-a_i)<=1/2 proves the advertised uniform bound.

The normalized second difference is only bounded above, not asserted to be nonpositive. Conversion back to ordinary coefficient differences is correct. In the expansion, gamma<=beta and q_(k+1)>=q_k make the middle term nonpositive. The exact underlying identity, checked independently, is

(k+1)(k+2) Delta^2 d_k = ((2k-N+2)^2-N-2)d_k - 2(2k-N+3)H_k + P_k-M_k.

Consequently inequality (6), the ratio T_k/d_k, and criterion (7) follow. The derivative of the left side of (7) is strictly greater than three for delta>=0, so the endpoint check proves concavity over the entire required interval. The simpler condition (8) is a valid sufficient condition.

### Splicing and analytic ranges

Concavity for h<=k<=k0-1 means Delta_h>=...>=Delta_k0. Strict negativity from k0 onward prevents a later return to positive differences. Together with the universal initial nondecrease through h, this proves unimodality without assuming it anywhere.

For N>=256, m=floor(log_2 N), the parity choice delta in {m+1,m+2} gives an integer k0. The bound F_m(N-1)<m+1/(m+1)<delta proves (4). The dyadic inequality (m+2)^2<=2^(m-1) is true at m=8 and preserved by induction, proving (8). These estimates also ensure h<k0<N, so all denominators and second-difference indices are valid.

The five finite rows cover every integer 23<=N<=255 exactly once. The polynomial P_s(N), all five endpoint values and derivatives, and the first-row inequality (N-1)(N-3)<1536 were independently algebraically checked. The remaining four first-difference bounds follow from their stated endpoint inequalities. Thus this range has an elementary analytic proof in addition to its exact arithmetic checks.

## Reproduction and independent computation

The supplied certificate was rerun successfully. It checked:

- 14,464 parameter tuples with 2<=N<=22.
- All 233 arithmetic cases with 23<=N<=255.
- 274 actual-graph tuples and 148,700 subsets through N=10.

Its output is independently reproduced in review_all_blades_reproduction.json. The finite enumeration includes every positive core size and every nonempty sorted positive partition of the remaining order, hence every blade count. I independently compared partition counts against a coin-change dynamic program and checked uniqueness of the generated partitions; every count matched. The inclusion-exclusion implementation and direct convolution have correct index bounds and zero-coefficient conventions.

An additional reviewer implementation constructs actual closed-neighborhood bitmasks and computes domination directly, without using missing-blade classifications for the counts. It checks the exact H identity, the exact ordinary second-difference identity above, every integer-alpha bound for alpha=0,...,N, and the positive-triple bound. It passed on 412 parameter graphs with N<=11, comprising 431,324 subsets and 1,377 upper-half layer checks.

Reviewer script: review_all_blades_counts.py.

Finite tests do not justify extrapolation; the analytic argument supplies all larger orders. The complete result may accurately be described as a computer-assisted proof of the whole stated clique-join family's unimodality, subject separately to priority review. Existing subcases should not be counted again as independent solved questions.

## Audited snapshot

- all_blades_proof.md SHA-256: 1f93fc7f480ab061db61b7fe37f2e1ccb0e7736a26924ee2c8827a972c6e36a9
- verify_all_blades.py SHA-256: 7f98782e9ff1ec0fbcda9484fbc09df38a8588163ae0d0fcbb3c344174d89b04
