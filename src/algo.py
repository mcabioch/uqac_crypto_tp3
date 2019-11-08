#!/usr/bin/python3

import random
import math
import sys
import MillerRabin

factors=[int(nb) for nb in range(3,100,2) if MillerRabin.is_Prime(nb)]

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
