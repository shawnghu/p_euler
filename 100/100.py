# last time i tried at this one it was pretty hard
# what we know:
# blue / (blue + red) is approximately 1 / sqrt(2)
# (blue, blue - 1) and (red, red - 1) have the same factors except for a single factor of 2
# to save typing time from now on let's let "red" mean the total number of balls.
# this tells us at least that red is 0 or 1 mod 4, since red * red - 1 needs to have at least two factors of 2
# in general, we can assert a lot of conditions on the state of blue or blue + red modulo every prime, but this is mostly not enough:
# it allows us to make faster checks on a given blue, red pair, but it's possible we need to check 10^10 pairs, so we need to
# be able to filter them out a priori

# ah crap
# b ( b - 1) = r ( r - 1)  / 2
# 2b^2 - 2b = r^2 - r
# 2(b - 1/2)^2 - 1/2 = (r - 1/2)^2 - 1/4
# multiply by 4
# 2(2b - 1)^2 = (2r - 1)^2 + 1
# x = 2r - 1, y = 2b - 1
# x^2 - 2y^2 = -1 for odd x and y. with x > y

# this is a "negative Pell's equation", see question 66... 

# now obviously x = 1, y = 1 is a solution, so that's the fundamental solution
# Wikipedia gives the recurrence x_k+1 = x1 * x_k + 2 * y1 * y_k, 
# y_k+1 = x1 * y_k + y1 * x_k

# since x_1 = 1, y_1 = 1, this simplifies to x_k+1 = x_k + 2y_k, y_k+1 = x_k + y_k

x = 1
y = 1
while True:
    x, y = x + 2 * y, x + y
    if x >= 2 * 10 ** 12 and x ** 2 - 2 * y ** 2 == -1:
        print((y + 1) // 2)
        break
