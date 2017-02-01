#bouncing ball example using euler integration 

# import stuff
from numpy import array, arange
from pylab import plot, show, xlim, ylim

# define evolution equations

g = 9.81

def deriv(P):
    x = P[0]
    y = P[1]
    vx = P[2]
    vy = P[3]
    ax = 0.0
    ay = -g
    return array([vx,vy,ax,ay],float)

# setup integration time and time resolution

t0 = 0.0
t1 = 10.0
N = 10000
dt = (t1-t0)/float(N)

tpoints = arange(t0,t1,dt)

# set up boundary conditions
# walls at x0, x1, y0, y1

x0 = 0.0
x1 = 5.0
y0 = 0.0
y1 = 3.0

# set up intial conditions

p = array([0.0, 2.0, 1.5, 0.2],float)

xpoints = []
ypoints = []

# iterate through steps
# using Euler integration

for t in tpoints:
        xpoints.append(p[0])
        ypoints.append(p[1])
        
        p += dt*deriv(p)
        
        # reflect off walls
        if p[0] < x0:
            p[0] = 2.0*x0 - p[0]
            p[2] = - p[2]
            
        if p[0] > x1:
            p[0] = 2.0*x1 - p[0]
            p[2] = - p[2]
            
        if p[1] < y0:
            p[1] = 2.0*y0 - p[1]
            p[3] = - p[3]
            
        if p[1] > y1:
            p[1] = 2.0*y1 - p[1]
            p[3] = - p[3]

# show results
xlim(x0 - 1, x1 + 1)
ylim(y0 - 1, y1 + 1)

# draw box
boxx = [x0,x1,x1,x0,x0]
boxy = [y0,y0,y1,y1,y0]
plot(boxx,boxy, 'k-')

#draw path
plot(xpoints,ypoints)
show()

