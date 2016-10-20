# comparing factorial function to exp(power(x,1.5)/2) using matplotlib

from numpy import log, exp, power
from matplotlib.pyplot import figure, subplots,twinx, plot, show


def factorial(x):
    placer = 1 
    for i in range(1, x+1):
        placer *= i 
    return placer

def dashed(x):
    return exp(power(x,1.5)/2)

# use linspace .. range produces a list..
x = range(0,21)
y1 = log(map(factorial,x))
y2 = map(dashed,x)

# subplots returns a tuple with a figure, and axes objects
fig, ax1 = subplots()

ax2 = ax1.twinx()
ax1.plot(x, y1, '-')
ax2.plot(x, y2, '--')
