from numpy import exp
from numpy import arange, zeros
from pylab import show, plot
# from 17.3.1 newman ex 6.13 


#binary search method: example 
x = arange(0.01,10.0,1.0)
g = zeros(len(x),float)

def g_x(x):
	return 5.0*exp( -x ) + x - 5.0

#accuracy, displays up to 12 digits
accuracy = 1e-12

#interval left hand and right hand ( binary tree) 
ll = 4.01 #lower bound
ul = 10.0 # upperbound



# get middle of every tree, evaluate at that middle point, then check the sign 


g1 = g_x(ll)
g2 = g_x(ul)

if (g1*g2) > 0:
    print "sorry this is not in teh interval you are looking for"

else:
	while( ul-ll ) > accuracy:

		#if interval is  small enough stop
		# subdivide 

		#divides into four - new upper upper, upper lower, upper lowe,r and lower lower, and midpoint 

		ll1 = ll 
		ul1 = (ll+ ul)/2.0 #midpoint of previous interval 

		ll2 = ul1
		ul2 = ul

		print "midpoint", ul1


		#check for sign changes 
		if (g_x(ll1)*g_x(ul1)) < 0: 
			#this is the correct interval 
			ll = ll1
			ul = ul1
		else:
			ll = ll2
			ul = ul2
		

print "answer is:", (ll + ul)/2.0
