import math

counter = 0
num, den = 3, 2
for i in range(999):
    num, den = num + 2 * den, num + den
    if math.floor(math.log(num, 10)) > math.floor(math.log(den, 10)):
        counter += 1
print(counter)

    
