# Unimodality for all clique joins with disjoint clique blades

Complete computer-assisted proof, 22 October 2026. An independent AI mathematical audit returned PASS; see `independent_all_blades_review.md`. This is not a human review, a Lean formalization, or an external peer-review certificate. Historical priority remains separately qualified below. Nothing has been published or externally transmitted.

## Theorem and exact scope

Let r≥1, t≥1, and a_1,...,a_t≥1 be integers. Then the domination polynomial of

G = K_r ∨ (K_{a_1} ∪ ... ∪ K_{a_t})

has a unimodal coefficient sequence.

The proof below is analytic for every order N≥23. Orders N≤22 are certified by an exhaustive, exact, standard-library-only Python program included separately. The enumeration includes every r and every blade count, not just four blades. In particular the theorem answers the unimodality part of the question following Rather's Theorem 2.16 for the whole stated family. It does not assert log-concavity of the full polynomial, which is false, or resolve domination-polynomial unimodality for all graphs.

The previous four-blade normalized-concavity theorem is a separate stronger special-family statement. Neither it nor the finite checks alone imply the present theorem.

## 1. Notation and basic identities

Write R for the core vertex set, A_i for the blade vertex sets, A=Σ_i a_i, and N=A+r. Write d_k for the number of dominating k-subsets and q_k=d_k/C(N,k). Binomial coefficients with an index outside their natural range are zero.

A vertex subset dominates if and only if it meets R or meets every blade. Consequently

D(x)=((1+x)^r−1)(1+x)^A + B(x),

where B(x)=∏_i((1+x)^{a_i}−1). Put b_k=[x^k]B(x).

Every k-subset containing a specified core vertex dominates, so

(1)  d_k ≥ C(N−1,k−1).

Every superset of a dominating set dominates. Counting incidences between the k- and (k+1)-layers gives

(N−k)d_k ≤ (k+1)d_{k+1},

and therefore q_{k+1}≥q_k. In particular d_0,...,d_h is nondecreasing, where h=ceil(N/2).

For a nondominating k-set S, let h(S) be the number of vertices x outside S for which S∪{x} dominates. Define H_k=Σ_S h(S), summing over nondominating k-sets. A second incidence count gives

(2)  (k+1)(d_{k+1}−d_k) = H_k−(2k+1−N)d_k.

All nondominating S avoid R. If exactly blade i is missed then h(S)=r+a_i; if at least two blades are missed then h(S)=r.

Throughout the bounds below k≥h. If k>A, no k-set can avoid R; hence H_k=0 and all the auxiliary counts below are zero. Thus conditional probabilities on k-subsets of the A blade vertices are only used when k≤A.

## 2. A first-difference bound

For an integer α≥0 and real u≥0 define

F_α(u)=α+u/((α+1)2^{α+1}),    F(u)=min_{α≥0}F_α(u).

The minimum exists. Each F_α is nondecreasing in u, so F is nondecreasing too.

Choose S uniformly among the k-subsets of the A blade vertices. Let u_i be the probability that S misses exactly blade i and no other blade. These events are disjoint, so Σ_i u_i≤1. Also

u_i ≤ P(S∩A_i=∅) = C(A−a_i,k)/C(A,k) ≤ (1−k/A)^{a_i} ≤ 2^{−a_i}.

The penultimate inequality follows by writing the ratio as the product, for j=0,...,a_i−1, of (A−k−j)/(A−j); if the numerator binomial is zero the inequality is immediate.

For each integer α≥0,

Σ_i a_i u_i
 ≤ α + Σ_{a_i>α}(a_i−α)2^{−a_i}
 ≤ α + A/((α+1)2^{α+1}) = F_α(A).

For the last step, when integer a>α the quantity (a−α)/(a2^a) is maximized at a=α+1. Indeed its ratio at a+1 versus a is

[a/(a+1)]·[(a+1−α)/(2(a−α))] < 1.

It follows that Σ_i a_i u_i≤F(A). By the preceding classification of h(S),

H_k = r(C(A,k)−b_k)+C(A,k)Σ_i a_i u_i
    ≤ (r+F(A))C(A,k).

Furthermore, for k≥N/2,

C(A,k)/C(N−1,k) ≤ 2^{−(r−1)}.

This follows from the same product estimate, excluding r−1 vertices from an (N−1)-element ground set. Since r≤2^{r−1} and F(A)≤F(N−1), we obtain the uniform bound

(3)  H_k ≤ (1+F(N−1))C(N−1,k).

Combining (1), (2), and (3), the sequence is strictly decreasing from any index k_0≥h satisfying

(4)  (2k_0+1−N)·k_0/(N−k_0) > 1+F(N−1).

Indeed the function (2k+1−N)k/(N−k) is increasing for integers h≤k<N, so the same comparison proves d_{k+1}<d_k for every k≥k_0. It suffices in (4) to replace F(N−1) by any particular F_α(N−1).

## 3. A second-difference bound

For h≤k≤N−2 sample uniformly an ordered triple (S,x,y), where |S|=k and x≠y lie outside S. Let f be the indicator of domination and set

Z=f(S∪{x,y})−f(S∪{x})−f(S∪{y})+f(S).

Each augmented set is uniform in its own layer; hence E[Z]=q_{k+2}−2q_{k+1}+q_k. Since domination is increasing, Z∈{−1,0,1}.

The positive triples are exactly those where S avoids R and misses precisely two blades i,j, while x,y belong to those two blades in either order. Let T_k be their number. If e_{ij,k} is the number of k-subsets of the blade vertices missing exactly i,j and meeting every other blade, then

T_k=Σ_{i<j}2a_i a_j e_{ij,k}.

Using 2a_i a_j≤a_i²+a_j², then enlarging the families being counted,

T_k ≤ Σ_i a_i² C(A−a_i,k)
    ≤ C(A,k)Σ_i a_i² 2^{−a_i}
    ≤ (A/2)C(A,k)
    ≤ ((N−1)/2)C(N−1,k).

Here a·2^{−a}≤1/2 for every positive integer a. Therefore

(5)  q_{k+2}−2q_{k+1}+q_k
     ≤ T_k/[C(N,k)(N−k)(N−k−1)].

Write δ=2k−N, β=(N−k)/(k+1), and γ=β(N−k−1)/(k+2). Expanding d_ℓ=C(N,ℓ)q_ℓ yields

d_k−2d_{k+1}+d_{k+2}
 = (1−2β+γ)d_k
   +2C(N,k)(γ−β)(q_{k+1}−q_k)
   +C(N,k)γ(q_{k+2}−2q_{k+1}+q_k).

Since q_{k+1}≥q_k and γ≤β, the middle term is nonpositive. Applying (5), and the identity

(k+1)(k+2)(1−2β+γ)=(δ+2)²−N−2,

gives

(6)  (k+1)(k+2)(d_k−2d_{k+1}+d_{k+2})
     ≤ ((δ+2)²−N−2)d_k+T_k.

Finally, (1) and the bound on T_k give

T_k/d_k ≤ ((N−1)/2)·(N−k)/k
        = ((N−1)/2)·(N−δ)/(N+δ).

Thus ordinary coefficient concavity holds at index k whenever

(7)  (δ+2)²+((N−1)/2)·(N−δ)/(N+δ) ≤ N+2.

The left side in (7), viewed as a real function of δ≥0, is strictly increasing: its derivative is

2(δ+2)−N(N−1)/(N+δ)² > 3.

In particular, to establish concavity for h≤k≤k_0−1, it suffices to check (7) at δ=2k_0−N−2. A simpler sufficient condition is

(8)  (2k_0−N)² ≤ (N+5)/2,

because (N−δ)/(N+δ)≤1.

## 4. Combining the bounds

If (4) holds at k_0 and (7) holds through k_0−1, then the differences d_{k+1}−d_k are nonincreasing from k=h through k=k_0, and are strictly negative from k=k_0 onward. Therefore they cannot change from negative back to positive. Together with the initial nondecrease through h, this proves unimodality.

### All N≥256

Let m=floor(log_2 N), so m≥8. Choose δ to be the one member of {m+1,m+2} having the same parity as N, and put k_0=(N+δ)/2. Then

F(N−1) ≤ F_m(N−1)
       < m+1/(m+1) < m+1 ≤ δ.

Since k_0>N/2, it follows that

(δ+1)k_0/(N−k_0) > δ+1 > 1+F(N−1),

which is (4). Also

δ² ≤ (m+2)² ≤ 2^{m−1} ≤ N/2 < (N+5)/2,

so (8) holds. The elementary inequality (m+2)²≤2^{m−1} holds at m=8, and propagates by induction because ((m+3)/(m+2))²<2 for m≥8. These arguments prove unimodality for every N≥256, without invoking Zhang's large-order theorem.

### All 23≤N≤255

The following five rows choose α and δ=2k_0−N. Ranges are inclusive and only the stated parity is used.

| N range | parity | α | δ |
|---|---|---|---|
| 23 to 41 | odd | 3 | 3 |
| 24 to 64 | even | 3 | 4 |
| 43 to 159 | odd | 4 | 5 |
| 66 to 254 | even | 4 | 6 |
| 161 to 255 | odd | 4 | 7 |

These rows cover every integer in the interval exactly once. They satisfy both (4), with F_α replacing F, and (7) at k=k_0−1.

For explicit elementary verification, with s=δ, condition (7) at k_0−1 is equivalent, after multiplication by the positive denominator 2(N+s−2), to

P_s(N):=N²+(3s−1−2s²)N−2s³+4s²+3s−6 ≥ 0.

For the five rows respectively, the smallest N is 23,24,43,66,161. The corresponding values P_s(N) are 284,14,160,450,12888, and the corresponding derivatives P_s'(N) are 36,27,50,77,244. Since the derivatives increase with N, concavity holds throughout each row.

For the first-difference comparison in the first row, it reduces to

(N−1)(N−3)<1536,

which holds since N≤41 and 40·38=1520. In each other row, δ>F_α(N−1), as is immediate from its largest N: these upper bounds are respectively 3+63/64<4, 4+158/160<5, 4+253/160<6, and 4+254/160<7. Consequently (4) holds there too.

The companion script additionally verifies every one of these 233 arithmetic cases using exact rational arithmetic, recording the positive first-difference and nonnegative concavity margins.

## 5. Exact certificate for orders N≤22

The file `verify_all_blades.py` is an executable finite certificate using only Python's standard library and integer or rational arithmetic. For each N=2,...,22, it enumerates r=1,...,N−1 and every nondecreasing positive integer partition of N−r. This is exhaustive because permuting the blade orders only relabels the graph. It allows every blade count t≥1. The case with no blade is a complete graph and is immediate from the binomial coefficients.

For each tuple the program computes every coefficient from the disjoint-class formula in Section 1 and checks that there is no increase after the first strict decrease. It independently recomputes the vector by inclusion–exclusion. In addition, for all tuples with N≤10 it constructs the actual closed neighborhoods and enumerates all vertex subsets to confirm the coefficient vector, independently of both polynomial formulas.

The completed certificate checks 14,464 parameter tuples through N=22. The independent actual-graph audit checks 274 tuples and 148,700 vertex subsets through N=10. The verified output is `verification_all_blades.json`; run:

`python verify_all_blades.py > verification_all_blades.json`

The finite check is part of the proof, not a heuristic extrapolation. All orders above its finite range were proved analytically in Section 4. No floating-point computation is used.

## Literature and novelty qualification

- Rather, *On domination polynomials of some graphs*, JCMCC 126 (2025), Theorem 2.16 and following question: https://combinatorialpress.com/article/jcmcc/volume%20126/on-domination-polynomials-of-some-graphs.pdf
- Existing project and its two-blade ULC and three-blade non-log-concavity results: https://github.com/Aurantium-47/clique-join-domination-polynomials
- Burcroff and O'Brien already cover all three-blade and odd-order four-blade graphs via upper domination number, as well as various high-core/high-degree cases: https://arxiv.org/html/2110.00709
- Zhang already proves unimodality of all graphs with a universal vertex and N≥8192: https://arxiv.org/html/2111.00641 . His first/second incidence ideas motivated the search for stronger bounds, but the present derivation includes all required identities and does not use his theorem.
- Omar supplies overlap-based criteria and a threshold-graph theorem: https://arxiv.org/html/2601.14494v1 . Those sufficient conditions do not cover the whole family. The separate independent four-blade review records exact examples and important exclusions from novelty claims.

The independent AI mathematical audit found this to be a complete proof of the whole-family unimodality statement. Historical novelty is not established merely by search failure, and no previously covered subfamily should be counted as a separate new solved problem. The audited snapshot is preserved unchanged in `audited_snapshot/`; the present copy changes only these status paragraphs.
