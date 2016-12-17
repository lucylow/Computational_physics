
# interpolation 
from numpy import loadtxt, arange, zeros
from pylab import *
#hist, show, figure, ylim, plot, savefig

y = loadtxt("testdata.txt",float)
x0 = arange(0.0,len(y))
w  = arange(0.0,len(y))

x = arange(0.0, float(len(y)-1), 0.001)
fx = zeros(len(x),float)

#for each sample x we want to plot
for k in range(0,len(x)):
#sum over data points x basis functions
    for i in range(0,len(y)):
        w[i] = 1.0
        for j in range(0,len(y)):
            if j != i:
                w[i] *= (x[k] - x0[j])/(x0[i] - x0[j])
        fx[k] += w[i]*y[i] 

plot(x0,y,'o')
xlim(-0.5,len(y)+0.5)
show()

xlim(-0.5,len(y)+0.5)
plot(x0,y)
plot(x0,y,'o')
show()

xlim(-0.5,len(y)+0.5)
plot(x,fx)
plot(x0,y)
plot(x0,y,'o')
show()
