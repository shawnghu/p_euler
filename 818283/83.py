# i think this one is just Dijkstra's algorithm

import numpy as np

with open('818283/matrix.txt', 'r') as f:
    matrix = np.array([list(map(int, line.split(','))) for line in f.readlines()])

'''
matrix = np.array([[131, 673, 234, 103, 18],
                   [201, 96, 342, 965, 150],
                   [630, 803, 746, 422, 111],
                   [537, 699, 497, 121, 956],
                   [805, 732, 524, 37, 331]])
'''
MATRIX_SIZE = 80

visited = np.zeros((MATRIX_SIZE, MATRIX_SIZE))
costs = np.ones((MATRIX_SIZE, MATRIX_SIZE)) * np.inf
costs[0, 0] = matrix[0, 0]

# what's really needed here is a priority queue with index access
# i think you can implement this with a min heap or something with similar log(n) pop,
# as well as a separate map(tree) to keep track of indices,
# but i think this is a bit overkill for this problem
# it's sufficient to just O(n^2) find the minimum cost node
num_iterations = 0
while not np.all(visited):
    effective_costs = costs + (visited * 10000000) # effectively remove visited nodes; can't use np.inf due to nan from 0 * inf
    x, y = np.unravel_index(np.argmin(effective_costs), effective_costs.shape)
    visited[x, y] = True
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < MATRIX_SIZE and 0 <= ny < MATRIX_SIZE:
            costs[nx, ny] = min(costs[nx, ny], costs[x, y] + matrix[nx, ny])


print(costs[MATRIX_SIZE - 1, MATRIX_SIZE - 1])
