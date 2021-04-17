# -*- coding: cp1252 -*-
from numpy import empty, sqrt, abs
from pylab import imshow, show, xlabel, ylabel, title, gray

def f(u,v):
    z = u**2 + v
    return z

def Mandelbrot(c):
    resposta = "Sim"
    z = f(0,c)
    tentativas = 100
    for i in range(tentativas): 
        if abs(z) >= 2:
            resposta = "Nao"
            break
        else:
            z = f(z,c)
    
    return resposta
# N é o número de pontos
N = 1000

# Se x e y vão de -2 a 2, então o lado do quadrado é 2-(-2) = 4
Lado = 4.0

#Para cada iteração, esse será o passo "caminhado" tanto por x quanto por y
passo = Lado/N

matriz = empty([N,N], int)
x_inicial = -2.0
y_inicial = -2.0

for i in range(N):
    y = passo*i + y_inicial
    for j in range(N):
        x = passo*j + x_inicial
        z = complex(x,y)
        if Mandelbrot(z) == "Sim":
            matriz[i,j] = 0
        else:
            matriz[i,j] = 1
imshow(matriz, origin="lower", extent = [-2,2,-2,2]) 
gray()
title("Conjunto de Mandelbrot")
xlabel("Re{c}")
ylabel("Im{c}")
show()
