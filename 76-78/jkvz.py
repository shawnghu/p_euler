'''
Another person's solution on the forum; I stole it to learn something from it
'''
from time import perf_counter
from sympy import primefactors	

PiningForTheFjords = perf_counter()

# after Indranil Ghosh, Jul 13 2017, found on https://oeis.org/A000607 
lst = [1, 0]
n = 2
while True:
    pp = sum(sum(primefactors(k)) * lst[n - k] for k in range(1, n + 1)) // n
    if pp > 5000:
    	print(n)
    	break	    	
    lst.append(pp)
    n += 1

PiningForTheFjords = perf_counter() - PiningForTheFjords
print(PiningForTheFjords, "sec")

