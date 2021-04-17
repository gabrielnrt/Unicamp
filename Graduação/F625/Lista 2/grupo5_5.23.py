# -*- coding: cp1252 -*-
from numpy import loadtxt, array, empty,sin, cos, pi, sqrt
from pylab import imshow, show, xlabel, ylabel, title, colorbar, jet, figure

#ITEM A
w = loadtxt("altitude.txt",float)


#RETORNA UMA LISTA COM AS DIMENSOES DO ARRAY, ONDE O 1º ELEMENTO É O Nº DE LINHAS, E O 2º É O Nº DE COLUNAS
q2 = w.shape
linhas = q2[0]
colunas = q2[1]

derivadaX = empty([linhas,colunas],float)
derivadaY = empty([linhas,colunas],float)
h = 30000 # DISTÂNCIA ENTRE UM PONTO E OUTRO NO GRID

for j in range(colunas):
    for i in range(linhas):
        #PARA A DERIVADA EM X:
        if i == 0: #USAR FORWARD
            derivadaX[i][j] = (w[i+1][j] - w[i][j])/h
        elif i == linhas - 1: #USAR BACKWARD:
            derivadaX[i][j] = (w[i][j] - w[i-1][j])/h
        else: #USAR DIFERENÇA CENTRAL:
            derivadaX[i][j] = (w[i+1][j] - w[i-1][j])/(2*h)

        #PARA A DERIVADA EM Y:
        if j == 0: #USAR FORWARD:
            derivadaY[i][j] = (w[i][j+1] - w[i][j])/h
        elif j == colunas - 1: #USAR BACKWARD:
            derivadaY[i][j] = (w[i][j] - w[i][j-1])/h
        else: #USAR DIFERENÇA CENTRAL:
            derivadaY[i][j] = (w[i][j+1] - w[i][j-1])/(2*h)


#ITEM B

def intensidade(phi,x,y):
    retorno = (x*cos(phi) + y*sin(phi))/sqrt(x**2 + y**2 + 1)
    return retorno

phi = pi/4
I = empty([linhas,colunas],float)
for j in range(colunas):
    for i in range(linhas):
        I[i][j] = intensidade(phi,derivadaX[i][j],derivadaY[i][j])

imshow(I)
colorbar()
xlabel("x (m)")
ylabel("y (m)")
title("Intensidade")
show()

#ITEM C

silicon = loadtxt("stm.txt",float)
q = silicon.shape
linhas = q[0]
colunas = q[1]
h = 2.5

DerivadaX = empty([linhas,colunas],float)
DerivadaY = empty([linhas,colunas],float)

for j in range(colunas):
    for i in range(linhas):
        #PARA A DERIVADA EM X:
        if i == 0: #USAR FORWARD
            DerivadaX[i][j] = (silicon[i+1][j] - silicon[i][j])/h
        elif i == linhas - 1: #USAR BACKWARD:
            DerivadaX[i][j] = (silicon[i][j] - silicon[i-1][j])/h
        else: #USAR DIFERENÇA CENTRAL:
            DerivadaX[i][j] = (silicon[i+1][j] - silicon[i-1][j])/(2*h)

        #PARA A DERIVADA EM Y:
        if j == 0: #USAR FORWARD:
            DerivadaY[i][j] = (silicon[i][j+1] - silicon[i][j])/h
        elif j == colunas - 1: #USAR BACKWARD:
            DerivadaY[i][j] = (silicon[i][j] - silicon[i][j-1])/h
        else: #USAR DIFERENÇA CENTRAL:
            DerivadaY[i][j] = (silicon[i][j+1] - silicon[i][j-1])/(2*h)

Ia = empty([linhas,colunas],float)
for j in range(colunas):
    for i in range(linhas):
        Ia[i][j] = intensidade(phi,DerivadaX[i][j],DerivadaY[i][j])
figure()
imshow(Ia)
colorbar()
title("Imagem STM")
show()