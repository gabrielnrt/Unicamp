from numpy import empty, abs
from pylab import imshow, show, xlabel, ylabel, title, colorbar, jet, hsv, figure
q1 = 1.0
x1 = 5.0
y1 = 0.0
r1 = complex(x1,y1)

q2 = -1.0
x2 = -5.0
y2 = 0.0
r2 = complex(x2,y2)

def E(x,y):
    X1 = x - x1
    Y1 = y - y1
    X2 = x - x2
    Y2 = y - y2
    m1 = X1**2 + Y1**2 ## Esse é o módulo ao quadrado da posição da partícula 1
    m2 = X2**2 + Y2**2 ## Esse é o módulo ao quadrado da posição da partícula 2

    
    r = complex(x,y)
    if r - r1 == 0 or r - r2 == 0:
        Ex = 0
        Ey = 1
    else:
        Ex = q1*X1*(m1**(-3/2)) + q2*X2*(m2**(-3/2))
        Ey = q1*Y1*(m1**(-3/2)) + q2*Y2*(m2**(-3/2))

    z = complex(Ex,Ey)
    modulo = abs(z)
    return modulo


N = 100
passo = 1

magnitude = empty([N,N], float)
x_inicial = -50.0
y_inicial = -50.0

for i in range(N):
    y = passo*i + y_inicial
    for j in range(N):
        x = passo*j + x_inicial
        
        magnitude[i][j] = E(x,y)

imshow(magnitude, origin="lower", extent = [-50.0,50.0,-50.0,50.0])
colorbar()
jet()
xlabel("x (cm)")
ylabel("y (cm)")
title("Razão E/K (C/cm²)")
figure()
imshow(magnitude, origin="lower", extent = [-50.0,50.0,-50.0,50.0])
hsv()
xlabel("x (cm)")
ylabel("y (cm)")
title("Direção de E/K")
show()
