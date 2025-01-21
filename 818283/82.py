import numpy as np
with open('818283/matrix.txt', 'r') as f:
    matrix = [list(map(int, line.split(','))) for line in f.readlines()]

# ad hoc solution, i think kind of only works for this exact kind of problem

matrix = np.array(matrix).T

costs = np.zeros((80, 80))
for i in range(80):
    if i == 0:
        costs[i, :] = matrix[i, :]
    else:
        costs[i, :] = costs[i-1, :] + matrix[i, :]
    while True:
        changed = False
        for j in range(80):
            if j == 0:
                if costs[i, j] > costs[i, j + 1] + matrix[i, j]:
                    costs[i, j] = costs[i, j + 1] + matrix[i, j]
                    changed = True
            elif j == 79:
                if costs[i, j] > costs[i, j - 1] + matrix[i, j]:
                    costs[i, j] = costs[i, j - 1] + matrix[i, j]
                    changed = True
            else:
                if costs[i, j] > min(costs[i, j - 1], costs[i, j + 1]) + matrix[i, j]:
                    costs[i, j] = min(costs[i, j - 1], costs[i, j + 1]) + matrix[i, j]
                    changed = True
        if not changed:
            break

print(min(costs[-1, :]))