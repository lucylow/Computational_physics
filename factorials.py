def factorial(n): 
	# factorial is the product of all positive integers less than or equal to n
	# 5! = 5*4*3*2*1 = 120
	f = 1.0
	for k in range(1,n+1):
		f *= k # also f= k*f
	return f 

a = factorial(10)
print a
