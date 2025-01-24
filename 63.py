import math
logs = [math.log(x, 10) for x in range(2, 10)] # anything 10 or above is disqualified for being too large, e.g 10 **3 is a 4th power already

counter = 1 # this is for 1 ** 1 being a 1-digit number
for x in range(1, 10000):
    for idx, log in enumerate(logs):
        if math.ceil(log * x) == x:
            print(str(idx + 2) + ' to the power of ' + str(x) + ' is a ' + str(x) + 'digit number: ' + str(log * x) + ' ' + str((idx + 2) ** x))
            counter += 1
print(counter)
