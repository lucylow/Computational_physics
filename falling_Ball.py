'''
Example 2: Falling ball 
	- Ball is dropped from a tower of height h. For input t, time - find the height it reaches 
	- physics formula: uniformly accelerated motion 

'''

height = float(input("Enter the height of the tower:"))
time = float(input("Enter the time interval:"))

seconds = (9.81*t**2)/2 # double check this equation

print "The height of the ball is", height-seconds, "meters"

''' 
