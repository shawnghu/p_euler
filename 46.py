from utils.prime_generator import naivePrimeGenerator
import itertools

primegen = naivePrimeGenerator()
firstprimes = itertools.islice(primegen, 100000)

squares = list((x ** 2 for x in range(1, 100000)))
diprime = {x: True for x in firstprimes}
print(squares)
# print('generated primes and squares')

check = 35
while True:
    if check % 1000000 == 1:
        print("checking: ", check)
    if check in diprime:
        check += 2
        continue
    counterexample = True
    for square in squares:
        if check == 45:
            print(square)
        if 2 * square > check:
            break
        if check - (2 * square) in diprime:
            counterexample = False
            break
    if counterexample:
        print('Found it!')
        print(check)
        break
    if check > 1000000000:
        print('1000000000')
        break
    check += 2
# ;primegen 
