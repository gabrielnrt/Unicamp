from numpy import empty, abs
from pylab import imshow, show, xlabel, ylabel, title, colorbar, jet

def phi(q,d):
    if d == 0:
        v = 0
    else:
        v = q/d
    return v

q1 = 1.0
x1 = 5.0
y1 = 0.0
r1 = complex(x1,y1)

q2 = -1.0
x2 = -5.0
y2 = 0.0
r2 = complex(x2,y2)

N = 100
passo = 1

V = empty([N,N], float)
x_inicial = -50.0
y_inicial = -50.0

for i in range(N):
    y = passo*i + y_inicial
    for j in range(N):
        x = passo*j + x_inicial        
        r = complex(x,y)
        
        d1 = abs(r-r1)
        phi1 = phi(q1,d1)
        
        d2 = abs(r-r2)
        phi2 = phi(q2,d2)

        if r-r1 == 0:
            V[i][j] = 1
        elif r-r2 == 0:
            V[i][j] = -1
        else:
            V[i][j] = phi1 + phi2

imshow(V, origin="lower", extent = [-50.0,50.0,-50.0,50.0])
colorbar()
jet()
xlabel("x (cm)")
ylabel("y (cm)")
title("Razão V/K (C/cm)")
show()
        
