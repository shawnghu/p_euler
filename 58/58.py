# I'm again on the wrong machine, and will assume a quick prime checker works.
# I was able to write this one in four minutes.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gencorners():
    x = 1
    toadd = 2
    while True:
        toyield = []
        for i in range(4):
            x += toadd
            toyield.append(x)
        toadd += 2
        yield toyield

successes = 0
trials = 1
side_length = 1
corner_generator = gencorners()
while True:
    side_length += 2
    corners = next(corner_generator)
    if is_prime(corners[0]):
        successes += 1
    if is_prime(corners[1]):
        successes += 1
    if is_prime(corners[2]):
        successes += 1
    if is_prime(corners[3]):
        successes += 1
    trials += 4
    if successes / trials < 0.1:
        print(successes / trials)
        print(side_length)
        break
