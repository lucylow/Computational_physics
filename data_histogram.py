from numpy import loadtxt
from matplotlib.pyplot import hist, show, title, xlabel, ylabel, grid

data = loadtxt("sampledata.txt",float) #array of floats 

grid()
xlabel("Number between 0-100")
ylabel("Frequency of Number")
title("Frequency of numbers in sampledata.txt")
hist(data)
show()
