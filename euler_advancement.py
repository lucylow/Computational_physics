from math import sin, pi 
from numpy import array, arange 
from pylab import plot, show, xlabel, ylabel
import matplotlib.pyplot as plt 

t0 = 0.0
t1 = 3.0
N = 3000000 # 3 million points to get good value  
h = (t1-t0)/N 

g = 9.81 # m/s/s
l = 0.1 #10cm 

tpoints = arange(t0,t1,h) # timem values stored here 
thpoints = [] # theta values stored here
opoints = [] # omega - angular velocity  valyes stored here 

# initial conditions 
theta0= 179.0*(pi/180) #starting angles 
omega0= 0.0*(pi/180) #starting velocity
r = array([theta0, omega0], float) # startign vevtor r

# for every time step... update time, calculate omega and addd it
# position and velcotiy needs to be updated using the old values 
for t in tpoints:
	thpoints.append(r[0])
	opoints.append(r[1])
	fomega = -(g/l)*sin(r[0]) # calaculate angular acceleratino 
	r[0] += h*r[1]
	r[1] += h*fomega


thdpoints = [180/pi*x for x in thpoints]

plot(tpoints, thdpoints) 

xlabel("t")
ylabel("theta in degrees")
show() 
