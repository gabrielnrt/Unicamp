from numpy import linspace, pi, cos, sin, e
from pylab import show, plot, xlabel, ylabel, title


theta = linspace(0, 24*pi, 1000)
r = e**(cos(theta)) -2*cos(4*theta) + sin(theta/12)**5

x = r*cos(theta)
y = r*sin(theta)

plot(x,y)
title("Função de Fey")
xlabel("Eixo x")
ylabel("Eixo y")
show()
