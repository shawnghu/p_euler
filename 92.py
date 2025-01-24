results = {1: 1, 89: 89}

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def squarify(num):
    total = 0
    while num > 0:
        total += squares[num % 10]
        num //= 10
    return total

counter = 0
for i in range(1, 10000000):
    if i % 100000 == 0:
        print(i)
    sequence = [i]
    while True:
        i = squarify(i)
        sequence.append(i)
        if i in results:
            for past_i in sequence:
                results[past_i] = results[i]
            if results[i] == 89:
                counter += 1
            break
print(counter)
