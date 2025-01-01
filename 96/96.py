import numpy as np
import sys
def parse_file(file_path):
    grids = []
    grid = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            if line.startswith('Grid'):
                if grid:
                    grids.append(np.array(grid))
                grid = []
            else:
                grid.append([int(c) for c in line.strip()])
        grids.append(np.array(grid)) # forgot the last grid; there won't be a new Grid line
    return grids

def increment_idx(idx, grid):
    new_idx = idx
    while True:
        new_idx += 1
        if new_idx == 81:
            return new_idx
        i = new_idx // 9
        j = new_idx % 9
        if grid[i, j] == 0:
            return new_idx

def decrement_idx(idx, grid):
    new_idx = idx
    while True:
        new_idx -= 1
        i = new_idx // 9
        j = new_idx % 9
        if grid[i, j] == 0:
            return new_idx

# After filling in the cell value at coordinates i, j,
# check if the constraints are still satisfied
# return True if yes and False if no
def check_constraints(grid, i, j):
    # row constraint
    for k in range(9):
        if k != j and grid[i, k] == grid[i, j]:
            return False
    # column constraint
    for k in range(9):
        if k != i and grid[k, j] == grid[i, j]:
            return False
    # 3x3 subgrid constraint
    for k in range(3):
        for l in range(3):
            if (i//3*3+k, j//3*3+l) != (i, j) and grid[i//3*3+k, j//3*3+l] == grid[i, j]:
                return False
    return True

# https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
# it turns out there are a lot of elegant solutions for this sort of thing,
# but sadly I think that it's possible to brute force this using the most naive algorithm

# There are even two ways to implement the simple recursion:
# 1. more elegant looking; break recursion down into just two cases
# (if a given cell is already solved, then we only need to recurse on one case,
# and if it's not solved, then we need to recurse on potentially all 9 cases)
# unfortunately, what will happen is you'll need to wait for a very long time 
# in order to hit any of the constraints that are obviously there if you look at the given grid

# 2. significantly more efficient; init constraints and recurse then
# that's what this is
def solve_sudoku_recursive(constraint_grid):
    def solve(grid, idx):
        if idx == 81:
            return grid
        i = idx // 9
        j = idx % 9
        # we have already guaranteed before the start of this loop that
        # the cell at coordinates i, j is not solved (i.e, is 0), so we can start incrementing
        while True:
            grid[i, j] += 1
            if grid[i, j] == 10:
                grid[i, j] = 0
                return None
            if not check_constraints(grid, i, j):
                continue
            res = solve(grid, increment_idx(idx, grid))
            if res is not None: # sentinel value for failure
                return res

    # init idx to the first cell that is not solved
    idx = 0
    if constraint_grid[0, 0] != 0:
        idx = increment_idx(idx, constraint_grid)
    return solve(constraint_grid, idx)

# this one is kind of dumb because i thought of it in highly mechanical terms and
# therefore came up with an iterative solution
def solve_sudoku_iterative(grid):
    # brute force search with backtracking
    new_grid = grid.copy()
    idx = 0
    if new_grid[0, 0] != 0:
        idx = increment_idx(idx, grid)
    while idx < 81:
        i = idx // 9
        j = idx % 9
        # we can assume that idx corresponds to a solvable cell
        new_grid[i, j] += 1
        if new_grid[i, j] == 10:
            new_grid[i, j] = 0
            idx = decrement_idx(idx, grid)
            continue
        if check_constraints(new_grid, i, j):
            idx = increment_idx(idx, grid)
    return new_grid


'''
# This doesn't work. Why did I think it would work?
# This is one of those things where I would've been able to tell that it wouldn't work
# if I had only asked myself the question "how could this possibly not work?"
def solve_sudoku(grid):
    # init potential values for each cell
    potential_values = np.ones((9, 9, 9), dtype=bool)
    solved = np.ones((9, 9), dtype=bool)
    num_solved = 0
    # apply constraints
    for i in range(9):
        for j in range(9):
            if grid[i, j] != 0:
                val = grid[i, j]
                # solve this cell, because it's already solved
                potential_values[i, j, :] = False
                potential_values[i, j, val] = True
                solved[i, j] = True
                num_solved += 1
                # constrain this row
                potential_values[i, :, val] = False
                # constrain this column
                potential_values[:, j, val] = False
                # constrain this 3x3 subgrid
                potential_values[i//3*3:(i//3+1)*3, j//3*3:(j//3+1)*3, val] = False
    # solve
    while True:
        for i in range(9):
            for j in range(9):
                if not solved[i, j]:
                    # check if there is only one potential value

    return grid
'''


def main():
    file_path = 'p096_sudoku.txt'
    sudoku_grids = parse_file(file_path)
    problem_sum = 0
    for grid in sudoku_grids:
        # solved_grid = solve_sudoku_recursive(grid)
        solved_grid = solve_sudoku_iterative(grid)
        # aw man, cursor autocompleted this line, so PE 96 is totally in the training set
        problem_sum += solved_grid[0, 0] * 100 + solved_grid[0, 1] * 10 + solved_grid[0, 2] 
    print(problem_sum)

if __name__ == '__main__':
    main()
