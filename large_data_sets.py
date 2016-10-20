 psize = size*size
 p_av = zeros(psize, float)

 for i in range(0,size):
 	for j in range(0,size):
 		if i != j:
 			p_av[(size*i) + j] = (marks[i]+marks[j])/ 2.0 
 		else:
 			p_av[(size*i)+ j] = 0
