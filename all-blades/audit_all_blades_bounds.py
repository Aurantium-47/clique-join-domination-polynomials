#!/usr/bin/env python3
"""Independent exact audit of proof inequalities, not needed for its finite certificate."""
from verify_all_blades import C,coefficients,partitions
from fractions import Fraction as F
from random import Random
import json


def weighted_missed(r,aa):
    A=sum(aa); p=[[1],[0],[0]];degree=0
    for a in aa:
        out=[[0]*(degree+a+1) for _ in range(3)]
        for m in range(3):
            for j,v in enumerate(p[m]):
                for z in range(1,a+1):out[m][j+z]+=v*C(a,z)
                if m<2:out[m+1][j]+=a*v
        p=out;degree+=a
    return p


def check(r,aa):
    A=sum(aa);N=A+r;d=coefficients(r,aa);b,e1,e2=weighted_missed(r,aa)
    alpha=min(range(N),key=lambda a:F(a)+F(N-1,(a+1)*2**(a+1)))
    M=F(alpha)+F(N-1,(alpha+1)*2**(alpha+1))
    checks=0
    for k in range((N+1)//2,N):
        bk=b[k] if k<=A else 0
        H=r*(C(A,k)-bk)+(e1[k] if k<=A else 0)
        assert (k+1)*(d[k+1]-d[k])==H-(2*k+1-N)*d[k]
        assert H<= (1+M)*C(N-1,k)
        if k<=N-2:
            T=2*e2[k] if k<=A else 0
            assert T<=F(A,2)*C(A,k)
            eta=2*k-N
            lhs=(k+1)*(k+2)*(d[k]-2*d[k+1]+d[k+2])
            rhs=((eta+2)**2-N-2)*d[k]+T
            assert lhs<=rhs,(r,aa,k,lhs,rhs)
        checks+=1
    return checks

cnt=0;checks=0
for N in range(2,23):
    for r in range(1,N):
        for aa in partitions(N-r):
            checks+=check(r,aa);cnt+=1
rng=Random(20261022)
for z in range(1000):
    r=rng.randrange(1,9);t=rng.randrange(1,18)
    aa=tuple(sorted(rng.randrange(1,10) for _ in range(t)))
    checks+=check(r,aa)
print(json.dumps({'exhaustive_tuples_N_le_22':cnt,'seed':20261022,'additional_random_tuples':1000,'index_cases':checks,'all_bounds_pass':True},indent=2))
