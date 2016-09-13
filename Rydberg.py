# Rydberg formula gives you the first few transitions of the Hydrogen atom 

R = 1.097e-2

for m in [1,2,3]:
	print("Series for m=", m)
	for k in [1,2,3,4,5]:
		n = m+k
		invlambda = R*(1/m**2 - 1/n**2)
		print " ", 1/invlambda," nm"
