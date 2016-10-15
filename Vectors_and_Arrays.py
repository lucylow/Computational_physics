
'''
Containers 
	- sort data into "sets" of elements 
	- two types of containers 
		- lists ( slow, flexible)
		- arrays  ( fast, rigid)


	1) lists
		- ordered set of elements 
		- int, float, complex 
		- elements of a list, r[0], r[1]
		- can set them individually r[0] = 2
		- set them through statements, or expressions 
		- special operations lists 
			- sum, max, min, len 
			- map 
			- xv new elements to lists ( OO method)
			- pop (remove) elements from a list 

	2) arrays (different than lists!!)

		** Used for vectors, matrices, images, etc **

		- number of elements is FIXED 
		- all elements must be the same type
		- arrays can be 2D, 3D, or higher 
		- can do arithmetic on WHOLE arrays at once 
		- array operatinos are faster
		- printout of arrays is different 
		
		- creating arrays 
			- numpy functions
			- ones, empty 
			- convert list to array 

		- reading arrays from a single/multiple column file
		

'''

# lists 
[0, 4, 5]
[0, 0.1, 1+3j]

x = 1
y = 2
r = [x,y]
print r
# if x or y changes later on, the list doesn't change 

r[0] = 2

#expressions for x, y coordinates 
x = 1 
y = 2 
r = [ x*2 , y+1/sqrt(y) ]

# find the magnitude of vector a:
a = [1.0, 3.0, 5.6]
magnitude = sqrt(a[0]*a[0] + a[1]*a[1] + a[2]*a[2])

sum[1,2,3] # returns the sum of the elements in common type --> 6

max[1,2,3] #returns max value --> 3

min[1,2,3] #returns min value --> 1

len[1,2,3] # returns the length or number of elements --> 3

#map : apply an operatino to ALL the elements of a list : NOTE in python 2, returns a list, but in python 3, returns an "iterator" where you need to convert to a list

logr = map(log,r) #python 2 

map(lambda x: x+1, [1,2,3]) # --> [2,3,4]

logr = list(map(log,r)) # python 3


# append something to our list r 
r = [1.0, 1.5, 2.1, 3.6]
r.append(5.6)
print r 

# append --> create a list from scratch 

# remove an element "pop"
r = [1.0, 1.5, 2.1, 3.6]
r.pop() # note r.pop(n) removes n element, but SLOW 
print r 


'''

	2) arrays (different than lists!!)

		** Used for vectors, matrices, images, etc **

		- number of elements is FIXED 
		- all elements must be the same type
		- arrays can be 2D, 3D, or higher 
		- can do arithmetic on WHOLE arrays at once 
		- array operatinos are faster
		- printout of arrays is different 
		
		- creating arrays 
			- numpy functions
			- ones, empty 
			- convert list to array 

		- reading arrays from a single/multiple column file

		- array operations 
			- dot product 
			- max, min, len 
			- size, shape
		

'''
# zeros array [0,0,0,0] fixedsize
from numpy import zeros, ones, empty # note differences in array formations 
a = zeros(4, float) 
print a 

#convert list to array
r = [1.0, 2.0, 4.0]
a = array(r, float) # array name and type 

# multi-dimensional array
from numpy import array 
a = array([ [1,2,3] , [4,5,6] ], int)
print a 


# mutli-dimensional array - elements indexed in order row, then column 
a = zeros([2,2], int) #prints out [[0 0][0 0]]
a [0,1] = 1
a [1,0] = -1
print (a) # prints out [[ 0  1][-1  0]]

# note need to account for fact that indexed starts at 0 


# read arrays from a single/mulitple column file

a = loadtxt("values.txt",float)

# perform operations on the whole array at once
a = array( [1.0,2.0,3.0] , float)
b = array([4.0,5.0,6.0], float)

c = a + b 
print c 

# Dot product ( to multiply the individual elements)
from numpy import array, dot
a = array( [1.0,2.0,3.0] , float)
b = array([4.0,5.0,6.0], float)

c = dot(a,b)
print c #32


# Check the size and shape of an array ( instead of max, min, len)
a = array([[1.0, 2.0, 3.0], [4.0,5.0,6.0]], float)
print a.size # --> 6
print a.shape # --> (2,3) prints out row-column
