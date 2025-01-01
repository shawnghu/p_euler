cache = {}

cache[(1, 0)] = 1
cache[(1, 1)] = 1

NUM_TURNS = 15 # set to 4 for "unit test"

for n in range(2, NUM_TURNS + 1):
    for k in range(n + 1):
        # cache[n, k]  is an int which represents the number of trials in which you get k blues after n pulls
        # on turn n, there are n red disks and 1 blue disk
        if k == 0:
            cache[(n, k)] = (cache[(n - 1, k)] * n) 
            continue
        if k == n:
            cache[(n, k)] = cache[(n - 1, k - 1)]
            continue
        cache[(n, k)] = (cache[(n - 1, k)] * n) + cache[(n - 1, k - 1)]

win_trials = sum([cache[(NUM_TURNS, x)] for x in range(NUM_TURNS // 2 + 1, NUM_TURNS + 1)])
total_trials = sum([cache[(NUM_TURNS, x)] for x in range(NUM_TURNS + 1)])

print(cache)

print(win_trials) # 9219406943
print(total_trials) # 20922789888000

from mpmath import mp
mp.dps = 100

print (mp.mpf(total_trials) / mp.mpf(win_trials)) # round this number down to get the answer