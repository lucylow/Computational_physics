'''
Example 1: Rydberg Equation used in Atomic Physics to find the wavelengths of spectra lines for Hydrogen atoms. 

	- inputs: R, m, n, R= constant, m and n are integers representing the principle quantum numbers of the orbitals occupied BEFORE/AFTER the quantum leap 

	- output: invlambda, the first few transitin wavelengths of the EM radiation emitted
'''


R= 1.097e-2

for m in [1,2,3]:
	print "Series for m=", m 

	for k in [1,2,3,4,5]: # WHERE K =5 COME FROM???
		n = m+k
		invlambda = R*(1/m**2-1/n**2)
		print " ",1/invlambda," nm"


'''
('Series for m=', 1)
  91.1577028259  nm
  91.1577028259  nm
  91.1577028259  nm
  91.1577028259  nm
  91.1577028259  nm
('Series for m=', 2)

'''
