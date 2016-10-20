# Plotting function cos(power(n,2.0)) /(1.0 + (power(n,2.0)))

from matplotlib.pyplot import plot, show, title, xlabel, ylabel,grid,xticks,yticks,xlim, ylim
from numpy import cos, power, linspace, arange

def function(n): 
	return cos(power(n,2.0)) /(1.0 + (power(n,2.0)))

x = linspace(-5,+5,10)
y = map(function,x)

xlabel("input")
ylabel("output of function")
ylim(-0.5,1.0)
xlim(-10,11)
title("Python plotting")
xticks(range(-10,11), range(-10,11))


plot(x,y,"r-")
show()
