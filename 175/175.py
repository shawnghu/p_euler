# here's a compact way of computing f(x):
# represent x in its binary expansion
# for all the 0s, the number of ways you can break down 1s using that 0 as space is the number of 1s to the left of that 0 + 1
# then take the product of all these numbers
# so 10 = 0b 1010 
# nvm this is incorrect, since it doesn't account for the fact that you can break down further conditional on breaking down something to the right
# 0b 1010 can be broken like 0b "122", which means breaking the 8 into 4 + 2 + 2 because the 2 was vacated by breaking it into 1 + 1.
# this representation suggests base-3 numbers somehow... 

# i guess the spirit of PE is experimental mathematics sometimes

def find_all(string, substring):
    return [i for i in range(len(string)) if string.startswith(substring, i)] # who knew this function existed?


def f(x):
    digits = bin(x)[2:]
    cache = {}
    def g(digits):
        if digits in cache:
            return 0
        cache[digits] = True
        total = 0
        for stidx in find_all(digits, "10"):
            total += g(digits[:stidx] + "02" + digits[stidx+2:])
        
        for stidx in find_all(digits, "20"):
            total += g(digits[:stidx] + "12" + digits[stidx+2:])
        return total + 1
    return g(digits)

for x in range(1, 100):
    print(x, bin(x), f(x))

# it must be possible to intentionally construct an x such that f(x) = n for a given n.