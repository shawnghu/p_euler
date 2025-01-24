squares = [x ** 2 for x in range(2, 5000000)];
disquares = {x: True for x in squares}

largest = 0
best_d = None
for d in range(2, 1001):
    if d % 20 == 0:
        print(d)
    if d in squares:
        continue # given in problem, no solutions exist
    broke = False
    for xsquared in squares:
        # print(xsquared)
        if (xsquared - 1) / d in disquares:
            # print('wow')
            if xsquared > largest:
                largest = xsquared
                best_d = d
                print(best_d)
                print(largest ** 0.5)
                broke = True
            break
    if not broke:
        print('got to the end of the squares range, so this method does not work')
print(best_d)
        
