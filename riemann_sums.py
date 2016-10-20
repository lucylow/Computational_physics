#use Riemann Sums to estimate a definite integral 


# from x=-2 to x=+2 
# f(x) = cos(power(x,2)) / (1 + power(x,2)) 

# We can evaluate a definite integral using Riemann Sums method 

from math import cos
from numpy import linspace, sum, power, array


# x--> from -2 to 2 
# divide the x-axis to 100 mini sections to make our dx BOX WIR 
dx = (4.0)/100 #float

#write out our x-axis ticks - need linspace.. floats 

x_list = linspace(-2,2-dx,100) # subtract dx since not in calculations

#integral 
def f(x):
    return cos(power(x,2))/ (1+ power(x,2))

# we have dx, x_list, and f(x)
# find y values for all the x_list values..
# used map but map ==> list --> need array 

y_list = map(f, x_list) #returns a list. but we want an array
y_list = array(y_list)


#one rectangle area
single_rec_area = dx * array(map(f,y_list))


#sum up all the areas 
print single_rec_area.sum()
