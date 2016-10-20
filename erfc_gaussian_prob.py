# EXAMPLE: CERN's fluke discovercies - variance

# Expriment was 5-sigma, then 4.9-sigma, then 5.9-sigma, find the ODDS of the discovery being a fluke 

from math import erfc, sqrt 
	# erfc = complementary error function

print 0.5*erfc(5/sqrt(2.0)), "or 1 in", 2.0/erfc(5/sqrt(2.0))/,1.0e6, "million"

print 0.5*erfc(4.9/sqrt(2.0)), "or 1 in ", 2.0/erfc(4.9/sqrt(2.0))/1.0e6, "million"

print 0.5*erfc(5.9/sqrt(2)), "or 1 in",  2.0/erfc(5.9/sqrt(2.0)) / 1.0e6, "million"

