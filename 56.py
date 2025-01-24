def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

largest = 0
for a in range(100):
    for b in range(100):
        x = sum_digits(a ** b)
        if x > largest:
            largest = x
print(largest)


