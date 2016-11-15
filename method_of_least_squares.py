from pylab import scatter, xlabel,ylabel, xlim, ylim, savefig, plot, title
from numpy import loadtxt, power

data = loadtxt("millikan.txt",float)  #Reads data points from milikan.txt file

Ex_counter,Ey_counter,Exx_counter,Exy_counter = 0,0,0,0  # Set counters to start at 0 for sums

# Calculate Ex, Ey, Exx, Exy - increment values to counters
for i in range(0,6):
    Ex_counter += data[i,0]
    Ey_counter += data [i,1]
    Exx_counter += (data[i,0] * data[i,0])
    Exy_counter += (data [i,1] * data[i,0])
Ex,Ey, Exx,Exy = Ex_counter/6,Ey_counter/6,Exx_counter/6,Exy_counter/6


# Slope m, and y-intercept c for the line of best-fit 
m = (Exy - Ex*Ey) / (Exx - power(Ex,2))
c = ((Exx*Ey) - (Ex*Exy)) / (Exx - power(Ex,2))

print "For the line of best-fit, the slope was",m,"and the intercept was",c,"."
print " "

# Evalutes mxi + c, and stores values in fit_data 
fit_data =[] 

for i in range (0,6):
    fit_data.append((m*data[i,0]) + c)

# Graph scatter plot dots, and the line of best fit
x = data[:,0]
y1 = data[:,1]
y2 = fit_data

scatter(x,y1) # from millikan.txt dataset 
plot(x,y2,"k-") # line of best fit 

title(" Millikan's experimental value for Planck's constant ")
xlabel(" Frequency (Hz)")
ylabel(" Voltage (eV) ")

savefig('figure.png')
