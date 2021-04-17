from numpy import linspace, pi, cos, sin
from pylab import show, plot, xlabel, ylabel, title

theta = linspace(0,10*pi,1000)
r = theta*theta

x = r*cos(theta)
y = r*sin(theta)

plot(x,y)
title("r = θ²")
show()
