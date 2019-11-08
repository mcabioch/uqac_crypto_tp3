#!/usr/bin/python3

import random
import math
import sys
import MillerRabin
import algo

factors=[int(nb) for nb in range(3,100,2) if MillerRabin.is_Prime(nb)]

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
    c=pow(m,e,n)
    plain=pow(c,d,n)
    print(plain==m)


def gen_exp(p,q):
    e=1
    prod=(p-1)*(q-1)
    n=random.randint(100,300)
    while(math.gcd(e,prod)!=1):
        e=gen_prime(n)
    return e

def gen_RSApq(n):
    x0=gen_prime(n//3)
    a=10**(n-n//3)
    b=a*100
    #on genere un grand nombre premier
    #puis on en cherche un de la forme k*x+1
    #ainsi p-1 ne sera pas seulement composé de petits facteurs
    k=random.randrange(a,b)
    x=k*x0+1
    while(x&1 and pow(2,x-1,x)!=1 and not MillerRabin.is_Prime(x)):
        x+=x0
    return x

def test_sfactor(x,n):
    prod=1
    for nb in factors:
        prod*=math.gcd(nb**((n//2)),x)
    return x/prod > 10**50

def gen_prime(n):
    if(n<200):
        n=200
    a=10**n
    b=a*10
    x=random.randrange(a,b)
    x|=1
    while(pow(2,x-1,x)!=1 or MillerRabin.is_Prime(x)==False):
        x+=2
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
