#!/usr/bin/env python3
"""Exact finite certificate for the all-blade theorem. Python 3, standard library only."""
from math import comb
from fractions import Fraction as F
from itertools import combinations
import json


def C(n, k):
    return comb(n,k) if 0 <= k <= n else 0


def partitions(n, smallest=1):
    if n == 0:
        yield ()
    for a in range(smallest,n+1):
        for rest in partitions(n-a,a):
            yield (a,)+rest


def coefficients(r, aa):
    A=sum(aa); N=A+r; b=[1]
    for a in aa:
        new=[0]*(len(b)+a)
        for j,v in enumerate(b):
            for ell in range(1,a+1):
                new[j+ell]+=v*C(a,ell)
        b=new
    return [C(N,k)-C(A,k)+(b[k] if k<len(b) else 0) for k in range(N+1)]


def coefficients_inclusion_exclusion(r, aa):
    A=sum(aa); N=A+r; e=[1]+[0]*A
    degree=0
    for a in aa:
        for s in range(degree,-1,-1):
            e[s+a]-=e[s]
        degree+=a
    return [C(N,k)+sum(e[s]*C(A-s,k) for s in range(1,A+1)) for k in range(N+1)]


def unimodal(d):
    falling=False
    for a,b in zip(d,d[1:]):
        if b<a:
            falling=True
        elif b>a and falling:
            return False
    return True


def direct_graph_coefficients(r,aa):
    N=r+sum(aa); full=(1<<N)-1; core=(1<<r)-1
    closed=[full]*r; offset=r
    for a in aa:
        block=((1<<a)-1)<<offset
        closed.extend([core|block]*a); offset+=a
    d=[0]*(N+1)
    for mask in range(1<<N):
        dominated=0
        for v in range(N):
            if mask>>v&1: dominated|=closed[v]
        if dominated==full: d[mask.bit_count()]+=1
    return d


# Rows give inclusive N-range, parity, alpha, delta=2*k0-N.
ROWS=[(23,41,1,3,3), (24,64,0,3,4), (43,159,1,4,5),
      (66,254,0,4,6), (161,255,1,4,7)]


def arithmetic_certificate():
    witnesses=[]
    for N in range(23,256):
        rows=[z for z in ROWS if z[0]<=N<=z[1] and N%2==z[2]]
        assert len(rows)==1, (N,rows)
        _,_,_,alpha,delta=rows[0]
        k0=(N+delta)//2; eta=delta-2
        M=F(alpha)+F(N-1,(alpha+1)*2**(alpha+1))
        first=F((delta+1)*k0,N-k0)-(1+M)
        concavity=N+2-delta**2-F(N-1,2)*F(N-eta,N+eta)
        assert first>0 and concavity>=0, (N,first,concavity)
        assert (N+1)//2<k0<=N-1
        witnesses.append({'N':N,'alpha':alpha,'delta':delta,
                          'first_difference_margin':str(first),
                          'concavity_margin':str(concavity)})
    return witnesses


def main():
    report={'finite_graph_certificate':[], 'arithmetic_certificate':arithmetic_certificate()}
    total=0; direct=0; subsets=0
    for N in range(2,23):
        count=0
        for r in range(1,N):
            for aa in partitions(N-r):
                assert aa and all(a>0 for a in aa) and tuple(sorted(aa))==aa
                d=coefficients(r,aa)
                assert d==coefficients_inclusion_exclusion(r,aa), (r,aa,'formula mismatch')
                assert unimodal(d), (r,aa,d)
                if N<=10:
                    assert d==direct_graph_coefficients(r,aa), (r,aa,'graph mismatch')
                    direct+=1;subsets+=1<<N
                count+=1;total+=1
        report['finite_graph_certificate'].append({'N':N,'tuples':count,'all_unimodal':True})
    report.update(total_graph_tuples_N_le_22=total,
                  direct_graph_tuples_N_le_10=direct,
                  direct_subsets_checked=subsets,
                  arithmetic_orders_checked=len(report['arithmetic_certificate']),
                  scope='Every positive core r and every nonempty sorted positive blade partition, any blade count. Reordering blades changes no graph.')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
