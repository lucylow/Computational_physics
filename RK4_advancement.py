from math import sin, pi 
from numpy import array, arange 
from pylab import plot, show, xlabel, ylabel
import matplotlib.pyplot as plt 

t0 = 0.0
t1 = 10.0
N = 1000 # RK4 
h = (t1-t0)/N 

g = 9.81 # m/s/s
l = 0.1 #10cm 

def f(r,t):
	theta = r[0]
	omgea = r[1]
	ftheta = omega
	fomega = -(g/l)*sin(r[0]) # calaculate angular acceleratino 
	return array([ftheta,fomega], float)

tpoints = arange(t0,t1,h) # timem values stored here 
thpoints = [] # theta values stored here
opoints = [] # omega - angular velocity  valyes stored here 

# initial conditions 
# theta0= 179.0*(pi/180) #starting angles 
theta0 = 150.0*(pi/180) 
omega0= 0.0*(pi/180) #starting velocity
r = array([theta0, omega0], float) # startign vevtor r

# for every time step... update time, calculate omega and addd it
# position and velcotiy needs to be updated using the old values 
for t in tpoints:
	thpoints.append(r[0])
	opoints.append(r[1])

	# for RK4 , take 4 derivatives 
	k1 = h*f(r,t)
	k2 = h*f(r + 0.5*k1, t+0.5)
	k3 = h*f(r + 0.5*k2, t+0.5*h)
	k4 = h*f(r + k3, t+h)

	r += (k1+2*k2+2*k3+k4)/6.0



thdpoints = [180/pi*x for x in thpoints]

plot(tpoints, thdpoints) 

xlabel("t")
ylabel("theta in degrees")
show() 
