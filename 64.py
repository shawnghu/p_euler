from mpmath import mp
import mpmath
'''
def try_period(n, sequence):
    print(sequence)
    sequence = sequence[:len(sequence) // n * n]
    for i in range(len(sequence) // n - 1):
        if sequence[i * n:i * (n + 1)] != sequence[i * (n + 1): i * (n + 2)]:
            return False
    return True
'''


# @profile
def find_period(n):
    inp = n
    if mpmath.frac(n) < 1e-12:
        # print ("???")
        return 0
    history = {}
    # test = {}
    for i in range(20000):
        n = mpmath.frac(n)
        # print(n)
        short = mpmath.nstr(n, 12)
        # print(n)
        # print(short)
        if short in history:
            # print(short)
            # print(test[short])
            return i - history[short]
        history[short] = i
        # test[short] = mpmath.nstr(n, 40)
        n = 1 / n
    print("failed to find period for input: ", inp ** 2)
    
mp.dps = 400

#print(find_period(mp.sqrt(2)))
#print(find_period(mp.sqrt(3)))
#print(find_period(mp.sqrt(13)))

# print(find_period(mp.sqrt(2311)))
# sys.exit()
counter = 0
for i in range(2, 10001):
    if i % 200 == 0:
        print(i)
    period = find_period(mp.sqrt(i))
    if period % 2 == 1:
        counter += 1
print(counter)
    
# print_rem(mp.sqrt(9541))

# print(find_period(mp.sqrt(9973)))
# print(find_period(mp.sqrt(3)))
# print(find_period(mp.sqrt(7)))

