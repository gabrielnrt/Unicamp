# -*- coding: utf-8 -*-
from numpy import pi, sqrt
from time import time

def f(u):
    v = sqrt(1 - (u**2))
    return v

def INTEGRAL(N):
    h = 2/N
    final = 0
    
    for k in range(N):
        x = -1 + (h*k)
        y = f(x)
        final = final + h*y
    
    return final


## Item a

N = 100
integral = INTEGRAL(N)    
I = pi/2
epsilon = abs(I - integral)
print("Item (a):")
print("O valor exato da integral é: ",I)
print("O valor obtido da integral foi: ", integral)
print("A precisão obtida (em módulo) foi ", epsilon)


## Item b

Delta_t = 0
while Delta_t <= 1:
    N = N*2
    t0 = time()
    integral = INTEGRAL(N)
    t1 = time()
    Delta_t = t1 - t0
epsilon = abs(I - integral)    
print()
print("Item (b):")    
print("Para que o programa fosse executado em menos de 1 segundo, tivemos o seguinte valor da integral:", integral)
print("A precisão obtida (em módulo) foi ", epsilon)