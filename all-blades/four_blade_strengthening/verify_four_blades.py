#!/usr/bin/env python3
"""Exact, dependency-free checks; finite evidence, not a proof of the theorem."""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb
from collections import Counter
import json

def binom(n,k): return comb(n,k) if 0<=k<=n else 0

def parts_fixed(n,t,lo=1):
    if t==0:
        if n==0: yield ()
        return
    for a in range(lo,n//t+1):
        for rest in parts_fixed(n-a,t-1,a): yield (a,)+rest

def coefficients(r,aa):
    A=sum(aa); N=A+r
    # Independent inclusion-exclusion count for all-blade transversals.
    c=[0]*(A+1)
    for mask in range(1<<len(aa)):
        s=A-sum(a for i,a in enumerate(aa) if (mask>>i)&1)
        sign=(-1)**mask.bit_count()
        for k in range(s+1): c[k]+=sign*comb(s,k)
    return [binom(N,k)-binom(A,k)+(c[k] if k<=A else 0) for k in range(N+1)]

def convolution_coefficients(r,aa):
    c=[1]
    for a in aa:
        out=[0]*(len(c)+a)
        for i,v in enumerate(c):
            for j in range(1,a+1): out[i+j]+=v*comb(a,j)
        c=out
    A=sum(aa);N=A+r
    return [binom(N,k)-binom(A,k)+(c[k] if k<len(c) else 0) for k in range(N+1)]

def is_unimodal(d):
    falling=False
    for a,b in zip(d,d[1:]):
        if b<a: falling=True
        if falling and b>a: return False
    return True

def configuration_check(r,aa,j):
    N=r+sum(aa); R=frozenset(range(r)); blades=[];start=r
    for a in aa: blades.append(frozenset(range(start,start+a)));start+=a
    V=frozenset(range(N))
    def f(S): return bool(S&R) or all(S&B for B in blades)
    P=[];M=[];Q=[]
    for ss in combinations(range(N),j):
        S=frozenset(ss)
        for x,y in permutations(V-S,2):
            z=int(f(S|{x,y}))-int(f(S|{x}))-int(f(S|{y}))+int(f(S))
            if z==1:P.append((S,x,y))
            if z==-1:M.append((S,x,y))
            if not S&R and sum(not S&B for B in blades)==1 and x in R and any(y in B and not S&B for B in blades):Q.append((S,x,y))
    qset=set(Q); incoming=Counter();minout=None
    for S,x,y in P:
        outgoing=set()
        for z in S:
            if all(bool((S-{z})&B)==bool(S&B) for B in blades):
                for u in R: outgoing.add(((S-{z})|{x},u,y))
        assert outgoing<=qset
        for q in outgoing:incoming[q]+=1
        minout=min(minout,len(outgoing)) if minout is not None else len(outgoing)
    assert len(P)<=2*len(Q)<=len(M)
    if P:
        if j>=4:
            assert minout>=r*(j-2)
            assert max(incoming.values())<=2*(N-r-j-1)
        else:
            assert j==3 and N==6 and r==1
            assert minout==2 and max(incoming.values())<=3
    return {'r':r,'blades':aa,'j':j,'P':len(P),'Q':len(Q),'M':len(M),'minimum_outdegree':minout,'maximum_indegree':max(incoming.values(),default=0)}

def omar_criterion(r,aa):
    N=r+sum(aa);k=(N+1)//2;A=sum(aa)
    sigma=sum(a*binom(A-a,k) for a in aa)
    # Maximum spanning tree on all vertex-neighborhood classes, expanded by size.
    neighborhoods=[(1<<N)-1]*r
    start=r; core=(1<<r)-1
    for a in aa:
        nb=core|sum(1<<z for z in range(start,start+a)); neighborhoods.extend([nb]*a);start+=a
    edges=sorted(((binom(N-(neighborhoods[u]|neighborhoods[v]).bit_count(),k),u,v) for u in range(N) for v in range(u+1,N)),reverse=True)
    parent=list(range(N))
    def find(u):
        while parent[u]!=u:parent[u]=parent[parent[u]];u=parent[u]
        return u
    tau=0
    for w,u,v in edges:
        u=find(u);v=find(v)
        if u!=v:parent[u]=v;tau+=w
    lhs=Fraction(sigma-tau,binom(N,k));rhs=Fraction(2*k+1-N,k+1)
    return {'r':r,'blades':aa,'N':N,'sigma_minus_tau':str(lhs),'threshold':str(rhs),'criterion_holds':lhs<=rhs}

def main():
    cases=ineq=0
    for N in range(5,51):
        for r in range(1,N-3):
            for aa in parts_fixed(N-r,4):
                d=coefficients(r,aa);h=(N+1)//2
                assert d==convolution_coefficients(r,aa)
                assert is_unimodal(d)
                for j in range(h,N-1):
                    b0,b1,b2=(comb(N,j+u) for u in (0,1,2))
                    assert d[j]*b1*b2-2*d[j+1]*b0*b2+d[j+2]*b0*b1<=0,(r,aa,j)
                    ineq+=1
                cases+=1
    configurations=[]
    for N in range(5,11):
        for r in range(1,N-3):
            for aa in parts_fixed(N-r,4):
                for j in range((N+1)//2,N-1):configurations.append(configuration_check(r,aa,j))
    # Five-blade normalized concavity really fails; this is not nonunimodality.
    r=1;aa=(1,1,1,1,5);d=coefficients(r,aa);N=len(d)-1;j=5
    second=sum(w*Fraction(d[j+i],comb(N,j+i)) for i,w in enumerate((1,-2,1)))
    assert second>0 and is_unimodal(d)
    report={'four_blade_parameter_tuples_N_le_50':cases,'normalized_concavity_inequalities':ineq,'direct_configuration_cases_N_le_10':len(configurations),'configuration_results':configurations,'omar_examples':[omar_criterion(1,(1,2,2,4)),omar_criterion(1,(1,1,2,5)),omar_criterion(1,(2,2,2,3)),omar_criterion(1,(1,2,2,6))],'five_blade_obstruction':{'r':r,'blades':aa,'N':N,'j':j,'normalized_second_difference':str(second),'unimodal':True}}
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
