from pylab import imshow, show, xlabel, ylabel, title, colorbar, jet, hsv, figure
from numpy import ones,copy,cos,tan,pi,linspace, e, log, exp, sin, empty, abs
from time import time

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

q = 100 
L = 10

def dEx(x,xl,y,yl): #Integrando da componente x
    X = x - xl
    Y = y - yl
    if X == 0 and Y == 0:
        u = 0
    else:
        u = q*X*((X**2 + Y**2)**(-1.5))*(sin(2*pi*xl/L))*(sin(2*pi*yl/L))
    return u

def dEy(x,xl,y,yl): #Integrando da componente y
    X = x - xl
    Y = y - yl
    if X == 0 and Y == 0:
        u = 0
    else:
        u = q*Y*((X**2 + Y**2)**(-1.5))*(sin(2*pi*xl/L))*(sin(2*pi*yl/L))
    return u

def E(x0,y0):
    N = 50 
    a1 = -L/2
    a2 = L/2
    x,wi = gaussxwab(N,a1,a2)
    y,wj = gaussxwab(N,a1,a2)
    Ex = 0.0
    Ey = 0.0
    for j in range(N):
        for i in range(N):
            Ex = Ex + wi[i]*wj[j]*dEx(x0,x[i],y0,y[j])
            Ey = Ey + wi[i]*wj[j]*dEy(x0,x[i],y0,y[j])

    z = complex(Ex,Ey)
    u = abs(z)
    return u

N = 100
passo = 1
campo = empty([N,N], float)
x_inicial = -50.0
y_inicial = -50.0

t0 = time()
for i in range(N):
    y = passo*i + y_inicial
    for j in range(N):
        x = passo*j + x_inicial
        
        campo[i][j] = E(x,y)
t1 = time()

print("O tempo de execução do programa foi de",(t1-t0)/60,"minutos.")
imshow(campo, origin="lower", extent = [-50.0,50.0,-50.0,50.0])
colorbar()
xlabel("x (cm)")
ylabel("y (cm)")
title("Módulo de E/K")
figure()
imshow(campo, origin="lower", extent = [-50.0,50.0,-50.0,50.0])
hsv()
xlabel("x (cm)")
ylabel("y (cm)")
title("Direção de E/K")
show()

