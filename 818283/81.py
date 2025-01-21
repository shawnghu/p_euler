import numpy as np
with open('818283/matrix.txt', 'r') as f:
    matrix = [list(map(int, line.split(','))) for line in f.readlines()]

min_cost = np.zeros((80, 80))
for i in range(80):
    for j in range(80):
        if i == 0 and j == 0:
            min_cost[i, j] = matrix[i][j]
        elif i == 0:
            min_cost[i, j] = matrix[i][j] + min_cost[i, j-1]
        elif j == 0:
            min_cost[i, j] = matrix[i][j] + min_cost[i-1, j]
        else:
            min_cost[i, j] = matrix[i][j] + min(min_cost[i-1, j], min_cost[i, j-1])

print(min_cost[79, 79])