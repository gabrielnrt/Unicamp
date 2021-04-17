from numpy import linspace, pi, cos, sin
from pylab import show, plot, xlabel, ylabel, title

theta = linspace(0,2*pi,100)
x = 2*cos(theta) + cos(2*theta)
y = 2*sin(theta) - sin(2*theta)
plot(x,y, "c--")
title("Deltoide")
xlabel("x = 2cos(t) + cos(2t)")
ylabel("y = 2sen(t) - sen(2t)")
show()
