# Four-blade clique joins: upper-half normalized concavity

Research note, 22 October 2026. Supplementary strengthening within the clique-join project.

## Result and scope

**Theorem.** Let

G = K_r ∨ (K_a ∪ K_b ∪ K_c ∪ K_d),

where r,a,b,c,d are positive integers, N=r+a+b+c+d, and d_k is the number of dominating k-subsets. Put q_k=d_k/binom(N,k) and h=ceil(N/2). Then

q_j - 2q_{j+1} + q_{j+2} ≤ 0   for every h ≤ j ≤ N-2.

Consequently (d_h,d_{h+1},...,d_N) is log-concave, and the full domination coefficient sequence is unimodal.

This does not settle arbitrary numbers of blades. Three-blade unimodality and odd-order four-blade unimodality already follow from Burcroff–O’Brien, Corollary 6.3, because the upper domination number here is the number of blades. The even-order four-blade conclusion fills the remaining parity of this complete four-blade subfamily, subject to further priority checking. The normalized concavity assertion is stronger than unimodality. No worldwide novelty claim is made.

## Counting formula

Write R for the central clique and A_1,...,A_4 for the disjoint blade vertex sets. A subset is dominating if and only if it intersects R or intersects all four blades. Thus, with A=N-r,

D_G(x)=((1+x)^r-1)(1+x)^A + ∏_{i=1}^4((1+x)^{a_i}-1).

In particular d_k>0 for 1≤k≤N, because every k-subset containing a fixed central vertex is dominating.

## Probabilistic interpretation of second differences

Fix j with h≤j≤N-2. Choose uniformly an ordered triple (S,x,y), where S is a j-subset of V(G), and x,y are distinct vertices outside S. Let f(T) be the indicator that T dominates G. Define

Z(S,x,y)=f(S∪{x,y})-f(S∪{x})-f(S∪{y})+f(S).

Each of S∪{x}, S∪{y}, and S∪{x,y} is uniform in its corresponding layer, so

E[Z] = q_{j+2}-2q_{j+1}+q_j.

The domination property is increasing. Therefore Z belongs to {-1,0,1}. Let P be the set of triples with Z=1 and let M be the set of triples with Z=-1. It suffices to prove |P|≤|M|.

A positive triple must have S∩R empty, S missing exactly two blades X and Y, x∈X and y∈Y (in this order), and S intersecting both other blades. Indeed, adding one central vertex would already dominate, and two noncentral vertices can repair exactly two missing blades only by meeting them separately.

Let Q consist of triples (T,u,v) with |T|=j, T∩R empty, T missing exactly one blade Y, u∈R, and v∈Y. Such a triple lies in M, as does its distinct reversal (T,v,u). The core-first and core-second collections are disjoint, hence

2|Q|≤|M|.

## A bipartite relation from P to Q

For p=(S,x,y)∈P, write X,Y for the blades containing x,y. Choose a vertex z∈S such that deleting z does not empty either blade met by S; call such a z removable. Choose any u∈R. Then define

T=(S\{z})∪{x},     q=(T,u,y).

The set T meets X and the two blades met by S, misses exactly Y, and has no central vertex. Hence q∈Q. Distinct choices of z,u for a fixed p yield distinct q. This defines an ordinary bipartite relation, with no multiplicities needed.

For any q=(T,u,y)∈Q, all predecessors are obtained by choosing a blade X≠Y whose intersection with T is a singleton {x}, and choosing a vertex z outside T in one of the other two blades, then setting S=(T\{x})∪{z}. These conditions are necessary, and they also suffice. For a fixed X the number of possible z is

N-r-|X|-|Y|-j+1 ≤ N-r-j-1,

because |X|,|Y|≥1. The number is nonnegative whenever such a predecessor exists.

### Main case: j≥4

Every positive S meets exactly two blades. At most two of its j selected vertices can be non-removable (one from each singleton intersection), so each p has degree at least

r(j-2).

Every T occurring in Q meets exactly three blades and has size j≥4. Therefore at most two of those intersections are singletons. If P is nonempty, j selected vertices, the r central vertices, and at least one vertex in each of the two missed blades are disjoint; hence N-r-j-1≥1. The preceding inverse description gives degree at most

2(N-r-j-1)

for every q.

Double-counting the relation yields

r(j-2)|P| ≤ 2(N-r-j-1)|Q|.

Since j≥ceil(N/2), we have N≤2j, and

N-r-j-1 ≤ j-r-1 ≤ r(j-2).

The second inequality is equivalent to (r-1)(j-1)≥0. Therefore |P|≤2|Q|≤|M|. If P is empty the same conclusion is immediate.

### Small case: j=3

Here N≥5 (four nonempty blades and a nonempty core), and N≤2j=6. If P is nonempty, its selected set meets exactly two blades and has three vertices. Their intersection sizes are 1 and 2, so exactly two selected vertices are removable. Also N≥j+r+2 forces N=6 and r=1. Thus every p has degree 2.

A set T in Q has three vertices in three blades, so it has three singleton intersections. For each candidate X the inverse count is at most

N-r-j-1=1.

Every q therefore has degree at most 3. Double-counting gives 2|P|≤3|Q|, in particular |P|≤2|Q|≤|M|. If P is empty there is nothing to prove. These are all possibilities because j≥h≥3.

Thus E[Z]≤0 throughout the claimed range.

## From normalized concavity to unimodality

For each internal index k of (q_h,...,q_N), the proved inequality says

q_k ≥ (q_{k-1}+q_{k+1})/2 ≥ sqrt(q_{k-1}q_{k+1}).

All these entries are positive, so the tail q-sequence is log-concave. The binomial coefficient sequence is positive and log-concave; multiplying the two inequalities shows that (d_h,...,d_N) is log-concave and therefore unimodal.

For completeness, all domination sequences are nondecreasing up to h: double-count the pairs (S,T) with S a dominating k-set, T a (k+1)-set, and S⊂T. Every such T is dominating, giving

(N-k)d_k ≤ (k+1)d_{k+1}.

For k<h we have N-k≥k+1, hence d_{k+1}≥d_k. Concatenating this increasing initial segment with the unimodal tail beginning at h proves unimodality of the full sequence.

## Literature coverage and boundaries

1. Rather, *On domination polynomials of some graphs*, JCMCC 126 (2025), Theorem 2.16 and following question, p.286. The displayed counting formula above agrees with that theorem. https://combinatorialpress.com/article/jcmcc/volume%20126/on-domination-polynomials-of-some-graphs.pdf
2. Existing project: https://github.com/Aurantium-47/clique-join-domination-polynomials. Its two-blade ULC and three-blade non-log-concavity results are not claimed as new here.
3. Burcroff and O’Brien, *Unimodality and Monotonic Portions of Certain Domination Polynomials*, arXiv:2110.00709, Corollary 6.3: Γ≤3 suffices in even order; Γ≤4 suffices in odd order. Here minimal dominating sets are central singletons or choices of exactly one vertex from each blade, so Γ=4. https://arxiv.org/html/2110.00709
4. Zhang, *Domination polynomial is unimodal for large graphs with a universal vertex*, arXiv:2111.00641, Theorem 1.2: every graph with a universal vertex and N≥8192 is already covered. https://arxiv.org/html/2111.00641
5. Omar, *New Perspectives on the Unimodality of Domination Polynomials*, arXiv:2601.14494, Theorem 15 gives an overlap-based sufficient criterion; threshold graphs are also covered. These hypotheses do not uniformly establish the even four-blade case. For r=1 and blade orders (1,2,2,6), N=12, exact maximum-spanning-tree evaluation gives σ_6−τ_6=23/66>1/7, so Theorem 15 fails. This graph has an induced 2K2 (choose two vertices from each K_2 blade), so it is not a threshold graph. The corresponding exact calculations are included in the verification script. https://arxiv.org/html/2601.14494v1

The method above genuinely stops at four blades: for five or more, a set T can have at least three singleton blade intersections, defeating the bound 2|Q|. The target normalized concavity assertion is itself false in general for five blades, including certain threshold examples; this does not imply nonunimodality. A new idea is needed to settle all t.

## Reproducible finite audit

Run `python verify_four_blades.py > verification_output.json` using Python 3 with no third-party packages. The completed run on 22 October 2026 checked all 118,574 tuples with sorted positive blade orders and N≤50; it verified 2,345,394 normalized-tail concavity inequalities, all full coefficient sequences for unimodality, and equality of coefficients computed independently by inclusion–exclusion and convolution. It also exhaustively checked the signed configurations and the P-to-Q relation in 142 parameter/index cases through N=10. These finite checks supplement, but do not replace, the general proof above.

The five-blade obstruction has (q_5,q_6,q_7)=(131/252,68/105,47/60), hence q_5−2q_6+q_7=1/126>0. This only refutes extending normalized tail concavity to arbitrary blade count.
