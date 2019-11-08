#!/usr/bin/python3

import random
import math
import sys
import MillerRabin

factors=[int(nb) for nb in range(3,10000,2) if MillerRabin.is_Prime(nb)]

def main():
    lenNb=random.randint(5,8)
    eps=random.randint(1,3)
    
    p=gen_RSApq(lenNb)
    q=gen_RSApq(lenNb+eps)
    n=p*q
    e=gen_exp(p,q)
    d=congru_equation(e,1,(p-1)*(q-1))
    
    m=random.randint(n/10,n)
    print(m)
    c=expModulaire(m,e,n)
    plain=expModulaire(c,d,n)
    print(plain==m)


def gen_exp(p,q):
    e=1
    prod=(p-1)*(q-1)
    n=random.randint(5,10)
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
    x|=1
    congruCompo=pow(2,x-1,x)
    while(congruCompo!=1 or not MillerRabin.is_Prime(x)):
        while(there_is_sfactor(x)):
            x+=x0
        congruCompo=pow(2,x-1,x)
    return x
    
def gen_prime(n):
    x=0
    if(n<1):
        n=1
    a=10**n
    b=a*100
    x=random.randrange(a,b)
    x|=1
    congruCompo=pow(2,x-1,x)
    while(congruCompo!=1 or not MillerRabin.is_Prime(x)):
        #es qu'on peut facilement diviser ce nombre (petit facteur)
        while(there_is_sfactor(x)):
            x+=2
        congruCompo=pow(2,x-1,x)
    return x

def factorPminus1(n):
    B=20
    a=2
    b=a%n
    b=pow(b,math.factorial(B),n)
    d=math.gcd(b-1,n)
    return 1<d and d<n

def there_is_sfactor(x):
    #si x est pair
    if(not x&1):
        return True
    #si x peut être divisé par un des petits nombres premiers
    for nb in factors:
        if(x%nb==0):
            return True
    return False

def expModulaire(x,puissance,modulo):
    x=x%modulo
    congruCompo=1
    #on exploite ici le fait que l'on calcule tous les (2^2^n)
    #et que l'on a la décomposition en base 2 de puissance
    while(puissance>0):
        if(puissance & 1):
            congruCompo=(congruCompo*x)%modulo
        puissance>>=1
        x=(x*x)%modulo
    return congruCompo

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
