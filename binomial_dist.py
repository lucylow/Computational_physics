from math import factorial
from numpy import power

def binomial(n,k):
	if k == 0:
		return 1
	else:
		binom =factorial(n)/factorial(k)/factorial(n-k)
		return float(binom)


def coinflip(n,k):
	# binomial probability function 
	return binomial(n,k) * ((power(0.5,k))*(power(0.5,n-k)))

coinflip(5,3)
# 0.3125
