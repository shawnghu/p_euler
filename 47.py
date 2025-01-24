from utils.prime_generator import naivePrimeGenerator
from utils.prime_utils import factorize
import itertools

primegen = naivePrimeGenerator()
firstprimes = list(itertools.islice(primegen, 10000))
 
check = 100000
streak = 0
while True:
    if len(set(factorize(check, firstprimes))) == 4:
        print(check, " has four factors: ", (factorize(check, firstprimes)))
        streak += 1
    else:
        streak = 0
    if streak == 3:
        print('!!!!!!!!!!!')
    if streak == 4:
        print(check)
        break
    check += 1
    if check == 300000:
        break
