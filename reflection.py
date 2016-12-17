from math import cos,sin,pi
from numpy import array,arange,sin,cos,linspace,zeros
from pylab import plot,show,ylim

#step 1

closedint = range(101) # 0 to 100, so 101 values 
x = (pi/100)*array(closedint,float)


plot(x,sin(x))
ylim(0.0,1.1)

#step 2
xt = 1.1
yt = sin(xt)
dx = 0.3
slope = cos(xt) # = dy/dx
normal = -1/slope
dy = dx*slope
dy2 = dx
dx2 = dy2/normal

tangx = array([xt - dx, xt, xt+dx],float)
tangy = array([yt - dy, yt, yt+dy],float)
plot(tangx,tangy,'k-')

normx = array([xt -dx2, xt, xt+dx2],float)
normy = array([yt -dy2, yt, yt+dy2],float)
plot(normx,normy,'k-')

show()
