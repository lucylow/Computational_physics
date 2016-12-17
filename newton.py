# working secant method.. (newton's method) 

#tolerance
tol=1e-10

#newton method - secants
def newton(func, x0):
	p0 = x0
	if x0 >= 0:
	    p1 = x0*(1 + 1e-4) + 1e-4
	else:
	    p1 = x0*(1 + 1e-4) - 1e-4
	q0 = func(*((p0,) ))
	q1 = func(*((p1,) ))
	for iter in range(50):
	    if q1 == q0:
	        if p1 != p0:
	            msg = "Tolerance of %s reached" % (p1 - p0)
	        return (p1 + p0)/2.0
	    else:
	        p = p1 - q1*(p1 - p0)/(q1 - q0)
	    if abs(p - p1) < tol:
	        return p
	    p0 = p1
	    q0 = q1
	    p1 = p
	    q1 = func(*((p1,) ))


#function 
def P(x):
	return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1


x1_array = [0.01, 0.15, 0.35, 0.6, 0.7, 0.9]

#print roots
for i in x1_array:
   print "The root is at", newton(P,i), "and f(x) at the root is", P(i)


