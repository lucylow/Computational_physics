# Finding the Earth - Moon Lagrange Point 
from numpy import arange, zeros, ones
from pylab import plot, show, ylim 

G = 6.674e-11
Me = 5.974e24 # mass earth
Mm = 7.348e22 # math moon 

R = 3.844e8 #earth moon distance 
w= 2.662e-6

k = w/G/Me
rs = arange(1e6, 5e8,1.01e5)
f = zeros(len(rs))


# set up Horizonatal and Vertical axis 

f0 = zeros(len(rs)) # array of zeros .. H line... becomes the x-axis ,, ( better way call line function)
f1 = ones(len(rs))
f1 = f1*3.844e8  #vertical axis.... some special values 

for i in range(len(rs)):
	r = rs[i]
	f[i] = G*Me/r/r - G*Mm/(R-r)/(R-r) - w*w*r 

#plot (x,y)... plot cycles through colours 
plot(rs,f)
plot(rs,f0)
plot(f1,f)

ylim(-0.1, 0.1)
show()
