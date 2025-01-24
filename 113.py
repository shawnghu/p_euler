import math

# Note: 0 doesn't count. Also, some numbers are both increasing and decreasing, e.g 33333.

def get_increasing(n):
    return math.comb(n + 9, 9) - 1 # this rules out 0

def get_decreasing(n):
    total = -n # this rules out 0
    for i in range(1, n + 1):
        total += math.comb(i + 9, 9)
    return total

def get_answer(n):
    return get_increasing(n) + get_decreasing(n) - 9 * n

print(get_increasing(2)) # should be 54, by manual calculation
print(get_decreasing(2)) # should be 63, by manual calculation
print(get_answer(2)) # unit test, correct answer should be 99
print(get_answer(6)) # correct answer should be 12951
print(get_answer(100))

'''
# There should be a word for this... but screw it
def fact_down(start, down):
    total = 1
    for x in range(down):
        total *= start
        start -= 1
    return total

total = 0
for i in range(1, 3):
    total += fact_down(i + 8, 8)

print(fact_down(10, 2))
print(total)

'''
