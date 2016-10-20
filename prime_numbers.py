# program that returns a list of all the prime numbers in n 
def factors(n):
	factorlist = [] 
	k = 2  #smallest prime number
	while k <= n :
		while n%k == 0:
			factorlist.append(k)
			n /= k 
		k += 1
	return factorlist 


def factorial(n):
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)
