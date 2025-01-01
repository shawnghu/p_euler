# I guess the conceit of this one is to find a heuristic so that you don't have to check all the numbers up to 10^9

def reverse(n):
    return int(str(n)[::-1])

def is_reversible(n):
    if n % 10 == 0:
        return False
    return all(c in '13579' for c in str(n + reverse(n)))

'''
# first pass: just a heuristic about the last digit and the first digit
# this will work, but it takes like 20 minutes on my laptop, so obviously doesn't count
s = 0
for i in range(1, 10**9):
    if i % 10**6 == 0:
        print(i)
    if i % 10 + int(str(i)[0]) % 2 == 0:
        continue
    if is_reversible(i):
        s += i
print(s)
'''


'''
for i in range(100000000, 1000000000):
    if is_reversible(i):
        print(i)
'''
'''
# given unit test
counter = 0
for i in range(1, 10**3):
    if i % 10 + int(str(i)[0]) % 2 == 0:
        continue
    if is_reversible(i):
        counter += 1
print(counter)
sys.exit()
'''

# observation: if the length of the number is even, then the number is reversible iff the respective pairs of digits sum to an odd number less than 10
# so the number of solutions is easy to calculate in closed form:
# for each of the digit-pair slots, conditioned on the first digit being 1, there are 5 choices for the second digit, and etc.
# there are 5 + 5 + 4 + 4 + 3 + 3 + 2 + 2 + 1 + 1 + 0 = 30 choices for the pair in total, or 20 when zeroes are not allowed (for the first pair)
# so for an 8-digit number, there are 25^4 solutions
# if the length is 1 mod 4, then there are 0 solutions. (I haven't bothered to deduce why to the level of a proof, but observed it just by running the code)
# if the length is 3 mod 4, there are some decently large number of solutions.
# this all falls out of an analysis you can do by just trying ot figure out what the contribution of the carried 1 is in the addition, and breaking it into cases
# anyway, since 90% of the numbers are 9 digits long, and 9% of the digits are 8 digits long, we can just do a brute force search for the first 1% of the numbers
counter = 0
for i in range(1, 10**7):
    if i % 10 + int(str(i)[0]) % 2 == 0:
        continue
    if is_reversible(i):
        counter += 1
print(counter)
counter += 30**3 * 20 # 8-digit numbers
print(counter)





