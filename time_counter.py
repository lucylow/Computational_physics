import time 
t0 = time.time() 
sum = 0.0 

for i in range(0,40000000):
	sum += i
print sum 

print time.time() - t0, "seconds wall time"
