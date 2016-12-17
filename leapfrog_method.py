# Solving differential equations
# leapfrog method solution 

from math import sin, pi, sqrt
from numpy import array,arange
from pylab import plot, show, xlabel, ylabel, axes, xlim, ylim, grid
import matplotlib.pyplot as plt

ty0 = 0.0
ty1 = 10.0
t0 = ty0*3.15569e7
t1 = ty1*3.15569e7
N = 100
h = (t1-t0)/N

G = 6.673e-11
M = 1.98e30

def f(r,t):
    x = r[0]
    y = r[1]
    vx = r[2]
    vy = r[3]
    d = sqrt(x*x + y*y)
    ax = -x*G*M/d/d/d
    ay = -y*G*M/d/d/d
    return array([vx,vy,ax,ay],float)

tpoints = arange(t0,t1,h)
xpoints = []
ypoints = []

#two points start off the same
r = array([1.49e11, 0.0, 0.0, 29800.0],float)
r2 = array([1.49e11, 0.0, 0.0, 29800.0],float)

#set r2 with RK4
t = t0
h2 = h/2.0
k1 = h2*f(r, t)
k2 = h2*f(r + 0.5*k1,t+0.5*h2)
k3 = h2*f(r + 0.5*k2,t+0.5*h2)
k4 = h2*f(r + k3,t+h2)
r2 += (k1+2*k2+2*k3+k4)/6.0

for t in tpoints:
	xpoints.append(r[0])
	ypoints.append(r[1])
        r += h*f(r2, t + h2)
        r2 += h*f(r, t + h)

xau = [x/1.496e11 for x in xpoints]
yau = [y/1.496e11 for y in ypoints]

#plot(xpoints, ypoints)
plot(xau, yau)

axes().set_aspect('equal', 'datalim')
xlim(-1.5,1.5)
ylim(-1.5,1.5)
xlabel("x (AU)")
ylabel("y (AU)")
#grid(2.0)
show()
