import math

for x in range (-100, 5000):
    n1 = math.sqrt(x + 100)
    n2 = math.sqrt(x + 268)
    if n1 % 1 == 0 and n2 % 1 == 0:
        print str(x) 

    
