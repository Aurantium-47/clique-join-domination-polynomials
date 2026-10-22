#!/usr/bin/env python3
"""Independent graph-level audit of the all-blade incidence identities and bounds."""
from math import comb
from fractions import Fraction
from verify_all_blades import partitions, coefficients

def C(n,k):
    return comb(n,k) if 0<=k<=n else 0

def run():
    graphs=layers=sets=0
    for N in range(2,12):
        for r in range(1,N):
            for aa in partitions(N-r):
                allv=(1<<N)-1; core=(1<<r)-1; closed=[allv]*r; start=r
                for a in aa:
                    block=((1<<a)-1)<<start; closed.extend([core|block]*a);start+=a
                dom=[False]*(1<<N); cover=[0]*(1<<N); d=[0]*(N+1)
                for S in range(1,1<<N):
                    low=S&-S;cover[S]=cover[S^low]|closed[low.bit_length()-1]
                    dom[S]=(cover[S]==allv)
                    d[S.bit_count()]+=dom[S]
                assert d==coefficients(r,aa)
                H=[0]*(N+1);P=[0]*(N+1);M=[0]*(N+1)
                for S in range(1<<N):
                    k=S.bit_count()
                    if not ((N+1)//2<=k<=N-2):continue
                    outside=[v for v in range(N) if not S>>v&1]
                    for x in outside:
                        fx=dom[S|1<<x]
                        if not dom[S] and fx:H[k]+=1
                        for y in outside:
                            if x==y:continue
                            z=int(dom[S|1<<x|1<<y])-int(fx)-int(dom[S|1<<y])+int(dom[S])
                            P[k]+=z==1;M[k]+=z==-1
                for k in range((N+1)//2,N-1):
                    delta=2*k-N
                    assert (k+1)*(d[k+1]-d[k])==H[k]-(delta+1)*d[k]
                    assert (k+1)*(k+2)*(d[k]-2*d[k+1]+d[k+2])==((delta+2)**2-N-2)*d[k]-2*(delta+3)*H[k]+P[k]-M[k]
                    # Every integer alpha supplies the claimed valid upper bound.
                    for alpha in range(N+1):
                        rhs=(1+Fraction(alpha)+Fraction(N-1,(alpha+1)*2**(alpha+1)))*C(N-1,k)
                        assert H[k]<=rhs,(r,aa,k,alpha,H[k],rhs)
                    assert P[k]<=Fraction(N-1,2)*C(N-1,k)
                    layers+=1
                graphs+=1;sets+=1<<N
    print({'graphs':graphs,'vertex_subsets':sets,'upper_half_layer_checks':layers,'result':'all identities and bounds passed'})
if __name__=='__main__':run()
