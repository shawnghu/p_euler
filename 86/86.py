
'''
def idx_generator():
    # a < b < c
    max_size = 1
    a = 1
    b = 1
    c = 1
    yield a, b, c
    while True:
        max_size += 1
        new_indices = []
        c = max_size
'''
squares = {x ** 2 for x in range(1, 100000)}
def check_shortest_int(a, b, c):
    # by convexity argument, this is always the shortest path if a <= b <= c
    return (a + b) ** 2 + c ** 2 in squares # is computing a hash function faster than sqrt + int check?


# trying to write the above led me to realize that there is just symmetry for the iteration:
# when you try a new max value c, you can just iterate over exactly all the values of a and b up to c
# and this covers all the cases already

'''
num_solutions = 0
c = 0
while True:
    c += 1
    if c % 1000 == 0:
        print(c)
    for b in range(1, c + 1):
        for a in range(1, b + 1):
            if check_shortest_int(a, b, c):
                num_solutions += 1
    if num_solutions > 1000000:
        break
print(c)
'''

# the above is fast enough, but there is probably a faster way:
# the question almost just boils down to asking how many pythagorean triples there are where the second number is beneath a certain threshold
# except that we have to count the number of unique ways for a + b to be made with a < b < c
