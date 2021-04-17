from numpy import e, linspace
from pylab import plot, show, xlabel, ylabel, title, legend, grid

def f(x,a):
    u = x**(a-1)
    v = e**(-x)
    y = u*v
    return y

def conjunto(a):
    x = linspace(0,5,100)
    y = f(x,a)
    return y
    


x = linspace(0,5,100)


y = conjunto(2)
plot(x,y, color = 'b', label = "a = 2") ##Curva Azul

y = conjunto(3)
plot(x,y, color = 'g', label = "a = 3") ##Curva Verde

y = conjunto(4)
plot(x,y, color = 'r', label = "a = 4") ##Curva Vermelha

grid(True)
xlabel("x")
ylabel("f(x)")
title("Integrando da função Gama para diferentes valores de a")
legend(loc='upper left')
show()
