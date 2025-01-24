import math
squares = [x ** 2 for x in range(2, 750000)]
disquares = {x: True for x in squares} 

# @profile
def compute_pairs():
    pairs = {} # a pair implies a triple, but storing just the first two allows for some other optimizations
    for idx_b, square_b in enumerate(squares):
        b = idx_b + 2
        if idx_b % 1000 == 0:
            print(idx_b)
        for idx_a in range(idx_b):
            a = idx_a + 2
            square_a = squares[idx_a]
            if (square_a, square_b) in pairs:
                continue
            square_c = square_a + square_b
            if square_c in disquares:
                c = math.sqrt(square_c)
                if a + b + c > 1500000:
                    break
                pairs[(square_a, square_b)] = True
                max_multiple = 1500000 // (a + b + c)
                for multiple in range(2, int(max_multiple) + 1):
                    multiple_sq = squares[multiple - 2]
                    pairs[(square_a * multiple_sq, square_b * multiple_sq)] = True
    return pairs

print(len(compute_pairs()))

