# -*- coding: cp1252 -*-
from numpy import empty, sqrt, abs
from pylab import imshow, show, xlabel, ylabel, title, colorbar

def f(u,v):
    z = u**2 + v
    return z

def numero_de_iteracoes(c):
    resposta = "Sim"
    z = f(0,c)
    tentativas = 100
    contador = 0
    for i in range(tentativas): 
        if abs(z) >= 2:
            resposta = "Nao"
            break
        else:
            z = f(z,c)
        contador = contador + 1    
    return contador
N = 2000
Lado = 4.0
passo = Lado/N
matriz = empty([N,N], int)
x_inicial = -2.0
y_inicial = -2.0

for i in range(N):
    y = passo*i + y_inicial
    for j in range(N):
        x = passo*j + x_inicial
        z = complex(x,y)
        matriz[i][j] = numero_de_iteracoes(z)
        
imshow(matriz, origin="lower", extent = [-2,2,-2,2]) 
colorbar()
title("Conjunto de Mandelbrot para N = 2000")
xlabel("Re{c}")
ylabel("Im{c}")
show()

