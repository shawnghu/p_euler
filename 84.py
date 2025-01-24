'''
I am very surprised that this didn't work. The idea behind this is that jail dominates the distribution, and with doubles becoming more common and the spread of possible outcomes being smaller, the spaces immediately following jail would get a lot of visits. I guessed that since 5 is the most likely roll and you can also roll more than once, the modal string would be something like 101516. The below confirmed that guess, but it's still not the right answer, so I guess I'll do a MDP thing.

Update: The correct answer is apparently 101524. I didn't account for the fact that 24 is unusually popular due to CH2. 
The example actually gave me a huge hint, because 24 is the second most popular tile for the 6-sided die case.
Therefore, without actually doing any of the MDP work, 102415 and 101524 would've been great guesses.

'''
'''
import random
cdf16 = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8]
def roll_two_dice():
    return cdf16[random.randint(0, 15)]

NUM_ROLLS = 5
d = {x: 0 for x in range(2, 8 * NUM_ROLLS + 1)} # this could be an array, but it's easier to read as a dict
for y in range(1000000):
    if y % 50000 == 0:
        print(y)
    total = 0
    for x in range(5):
        total += roll_two_dice()
        d[total] += 1
print(d)
'''

'''
Note: There's at least one bug in the below, because it doesn't produce the right result for the six-sided die case, but it does for the problem specified.
Update again: Having read the forum, the "bug" is probably that the problem spec omits the fact that you reset the doubles counter when you go to jail for any reason,
so you won't go to jail as often as I've calculated here.

Another fun thing to note is that most solutions I found didn't calculate the stationary distribution by finding eigenvectors, but instead approximated it by simulation. Apparently simulation of the distribution easily converges in a few tens of thousands of iterations. This surprised me because I was thinking of directly simulating state evolution, but if you have a probabilistic state this makes a lot more sense.
'''

import numpy as np
import scipy
import pdb
THIRD_DOUBLE_CHANCE = 1 / 216
GO_IDX = 0
JAIL_IDX = 10
roll_dist = np.array([1 / 16, 2 / 16, 3 / 16, 4 / 16, 3 / 16, 2 / 16, 1 / 16])
# roll_dist = np.array([1 / 36, 2 / 36, 3 / 36, 4 / 36, 5 / 36, 6 / 36, 5 / 36, 4 / 36, 3 / 36, 2 / 36, 1 / 36])
roll_mdp = np.zeros((40, 40))
for x in range(40):
    for idx in range(len(roll_dist)):
        roll_mdp[(x + idx + 2) % 40, x] += roll_dist[idx]

CC_SPACES = [2, 17, 33]
cc_mdp = np.eye(40)
for space_idx in CC_SPACES:
    cc_mdp[[GO_IDX, JAIL_IDX], space_idx] = 1 / 16
    cc_mdp[space_idx, space_idx] = 14 / 16


CH_SPACES = [7, 22, 36]
ch_mdp = np.eye(40)
for space_idx in CH_SPACES:
    ch_mdp[GO_IDX, space_idx] = 1 / 16
    ch_mdp[JAIL_IDX, space_idx] = 1 / 16
    ch_mdp[11, space_idx] = 1 / 16
    ch_mdp[24, space_idx] = 1 / 16
    ch_mdp[39, space_idx] = 1 / 16
    ch_mdp[5, space_idx] += 1 / 16
    next_utility = 28 if (space_idx >= 12 and space_idx < 28) else 12
    ch_mdp[next_utility, space_idx] = 1 / 16
    if space_idx >= 5 and space_idx < 15:
        next_railroad = 15
    elif space_idx >= 15 and space_idx < 25:
        next_railroad = 25
    elif space_idx >= 25 and space_idx < 35:
        next_railroad = 35
    else:
        next_railroad = 5
    ch_mdp[next_railroad, space_idx] += 1 / 8
    ch_mdp[space_idx - 3 % 40, space_idx] = 1 / 16
    ch_mdp[space_idx, space_idx] = 6 / 16

go_to_jail_mdp = np.eye(40)
go_to_jail_mdp[10, 30] = 1
go_to_jail_mdp[30, 30] = 0

double_mdp = np.eye(40) * (1 - THIRD_DOUBLE_CHANCE)
double_mdp[JAIL_IDX, :] = THIRD_DOUBLE_CHANCE
double_mdp[JAIL_IDX, JAIL_IDX] = 1

mdp = np.matmul(double_mdp, np.matmul(go_to_jail_mdp, np.matmul(ch_mdp, np.matmul(cc_mdp, roll_mdp))))

'''
eig1 = np.linalg.eig(roll_mdp)
eig2 = np.linalg.eig(ch_mdp)
eig3 = np.linalg.eig(cc_mdp)
eig4 = np.linalg.eig(double_mdp)

eigs = np.linalg.eig(mdp)
'''
eigs = scipy.sparse.linalg.eigs(mdp, 3)
eigenvector = eigs[1][:, 0]
total = sum(eigenvector)
eigenvector /= total
print(eigenvector)
toprint = sorted(enumerate(eigenvector), key=lambda x: x[1], reverse=True)
print(toprint)
pdb.set_trace()
