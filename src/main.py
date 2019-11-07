#!/usr/bin/python3

import random
import math
import sys
import MillerRabin

factors=[int(nb) for nb in range(2,100) if MillerRabin.is_Prime(nb)]

def main():
    lenNb=random.randint(200,210)
    eps=random.randint(1,10)
    
    p=gen_RSApq(lenNb)
    q=gen_RSApq(lenNb+eps)
    n=p*q
    e=gen_exp(p,q)
    d=congru_equation(e,1,(p-1)*(q-1))
    
    m=random.randint(10**100,10**200)
    print(m)
    c=(m**e)%n
    plain=(c**d)%n
    print(plain==m)


def gen_exp(p,q):
    e=1
    prod=(p-1)*(q-1)
    n=random.randint(100,900)
    while(math.gcd(e,prod)!=1):
        e=gen_prime(n)
    return e

def gen_RSApq(n):
    x=gen_prime(n)
    while(not test_sfactor(x,n)):
        x=gen_prime(n)
    return x
    
def test_sfactor(x,n):
    prod=1
    for nb in factors:
        prod*=math.gcd(nb**((n//2)),x)
    return x/prod > 10**50

def gen_prime(n):
    x=0
    if(n<200):
        n=200
    a=10**n
    b=a*10
    while(x==0 or x&1!=1 or MillerRabin.is_Prime(x)==False):
        x=random.randrange(a,b)
    return x

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def congru_equation(a,b,n):
    """return x such that (x * a) % n == b"""
    result = 1
    g,x,_=xgcd(a,n)
    if g == 1:
        return (x*b) % n
    elif b%g == 0:
        b=b//g
        n=n//g
        a=a//g
        _,x,_=xgcd(a,n)
        return (x*b) % n 

if __name__ == "__main__":
    main()
