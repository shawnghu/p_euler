import bisect
import math
import numpy as np
import pdb
import itertools

import psutil
import resource

virtual_memory = psutil.virtual_memory()
available_memory = virtual_memory.available
mem_limit = int(available_memory * 0.8)
resource.setrlimit(resource.RLIMIT_AS, (mem_limit, mem_limit))

def successiveOddNumberTestingGenerator():
    primes = [2, 3, 5, 7, 11, 13]
    for i in primes:
        yield i

    check = 15
    while True:
        sqrt = math.sqrt(check) 
        checkisprime = True
        for prime in primes:
            if prime > sqrt:
                break
            if check % prime == 0:
                checkisprime = False
                break
        if checkisprime:
            yield check
            primes.append(check)
        check += 2

# no optimizations for space optimizations for small primes
# 15485863 is the 1 millionth prime
def naiveSieveOfEratosthenes(up_to=15485863):
    numbers = np.full(up_to + 2, True)
    numbers[0:2] = False
    primes = []
    idx = 2
    while idx < len(numbers) - 1:
        if numbers[idx]:
            primes.append(idx)
            numbers[::idx] = False
        idx += 1
    return primes

def naiveSieveOfEratosthenesOnOdds(up_to=15485863):
    numbers = np.full(up_to // 2, True)
    primes = [2]
    idx = 0
    while idx < len(numbers) - 1:
        if numbers[idx]:
            value = idx * 2 + 3
            primes.append(value)
            numbers[idx::value] = False
        idx += 1
    return primes

# Perhaps locality of reference would be improved if we folded both of these into the same array and did careful index math.
# I am not really sure how to generalize the index math for reducing the amount of space this takes;
# probably it will radically increase the amount of computation anyway.
def naiveSieveOfEratosthenesMod6(up_to=15485863):
    onesmod6 = np.full(up_to // 6, True)
    onesmod6[0] = False # hack, ensure that we can do the test for prime = 5 without looking at prime = 6 * 0 + 1
    fivesmod6 = np.full(up_to // 6, True)
    primes = [2, 3]
    for idx in range(len(onesmod6)):
        if onesmod6[idx]:
            value = 6 * idx + 1
            onesmod6[idx::value] = False
            fivesmod6[((value * 5) // 6)::value] = False
            primes.append(value)
        if fivesmod6[idx]:
            value = 6 * idx + 5
            fivesmod6[idx::value] = False
            onesmod6[((value * 5) // 6)::value] = False
            primes.append(value)
    return primes

# size of my L2 cache is 512k
# naive in that it doesn't optimize for odd numbers
# i accidentally optimized it quite a bit with a profiler so it's not that naive, and this thing is kinda misnamed, but oh well
#@ profile
def naiveSegmentedSieveOfEratosthenes(up_to=15484863, page_size=None):
    if page_size is None:
        page_size = math.floor(math.sqrt(up_to)) + 1
    num_pages = up_to // page_size + 1
    primes = naiveSieveOfEratosthenesMod6(page_size)
    for page_idx in range(1, num_pages):
        page = np.full(page_size, True)
        min_val = page_idx * page_size
        max_val = (page_idx + 1) * page_size
        '''
        for prime in primes:
            if prime > math.floor(math.sqrt(max_val)):
                break
        '''
        max_prime_check = math.floor(math.sqrt(max_val))
        max_prime_idx = bisect.bisect(primes, max_prime_check)
        for prime in primes[:max_prime_idx]:
            negative_offset = min_val % prime
            if negative_offset == 0: # seems kinda ugly, but what can you do
                first_idx = 0
            else:
                first_idx = prime - negative_offset
            page[first_idx::prime] = False
        for idx, value in enumerate(page):
            if value:
                primes.append(min_val + idx)
    return primes

# @profile
# For the first 10 million primes, almost 90 percent of the runtime of this algorithm is actually on iterating over the values in the page at the end.
# If we trust the above result, then the only way to get straightforward sieve methods to go faster is 
# to improve their space efficiency with some modular arithmetic/representation tricks.
# update: this is called wheel factorization
# there may be interest in implementing e.g the sieve of pritchard for values between like 1e9 and 1e15
# another thing of note is that for values like 1e11, there are something like 0.8e10 primes below that, which is harsh on memory requirements no matter what
# problems that require working with the set of primes of 9 or 10 digits will need to take a different approach from just storing them
def segmentedSieveOfEratosthenesOnOdds(up_to=15484863, page_size=None):
    if page_size is None:
        page_size = math.floor(math.sqrt(up_to)) // 2 + 1
    num_pages = up_to // 2 // page_size + 1
    primes = naiveSieveOfEratosthenesMod6(page_size * 2 + 1)
    page = np.empty(page_size)
    for page_idx in range(1, num_pages):
        page[:] = True
        min_val = page_idx * page_size * 2
        max_val = (page_idx + 1) * page_size * 2 + 1
        max_prime_check = math.floor(math.sqrt(max_val))
        max_prime_idx = bisect.bisect(primes, max_prime_check)
        for prime in primes[1:max_prime_idx]:
            residual = min_val % (prime * 2)
            if residual < prime:
                first_idx = (prime - residual) // 2
            else:
                first_idx = (prime * 3 - residual) // 2
            page[first_idx::prime] = False
        for idx, value in enumerate(page):
            if value:
                primes.append(min_val + (idx * 2) + 1)
    return primes

def main():
    # primegen = successiveOddNumberTestingGenerator() # 19 minutes 21 seconds for 10 million primes
    # firstprimes = np.array(list(itertools.islice(primegen, 10000000)))
    #np.save('first_million_primes', firstprimes)
    #np.save('first_10million_primes', firstprimes)
    # check = naiveSieveOfEratosthenes(179424673) #4.167 seconds for 1m primes, 63 seconds for 10m primes
    #check = naiveSieveOfEratosthenesOnOdds() # 2.82 seconds for 1m primes
    #check = naiveSieveOfEratosthenesOnOdds(179424673) # 28.21 seconds for 10m primes
    # primes = naiveSieveOfEratosthenesMod6() # 2.416 seconds for 1m primes
    # check = naiveSieveOfEratosthenesMod6(179424673) # 21.5 seconds for 10m primes
    #check = naiveSieveOfEratosthenesMod6(179424673) # 28.21 seconds for 10m primes
    # first_10m_primes = np.load('/home/shawnghu/project_euler/utils/first_10million_primes.npy')
    # primes = naiveSieveOfEratosthenesMod6(10000000000) # will crash due to OOM
    # primes = naiveSegmentedSieveOfEratosthenes() # for 1m primes, also about 2.4 seconds
    # primes = naiveSegmentedSieveOfEratosthenes(179424673) # for 10m primes, 30.6 seconds
    # it was at this time that i realized that the variance in times is greater than i thought
    # primes = naiveSegmentedSieveOfEratosthenes(179424673, page_size=65536) # 15-18 seconds
    # primes = naiveSegmentedSieveOfEratosthenes(179424673, page_size=131072) # 12-15 seconds, surprising me
    # primes = naiveSegmentedSieveOfEratosthenes(179424673, page_size=524288) # 16-17 seconds
    # primes = naiveSegmentedSieveOfEratosthenes(179424673, page_size=16378) # 32.5 seconds
    # primes = naiveSegmentedSieveOfEratosthenes(179424673, page_size=16378) # 16.8
    #primes = naiveSegmentedSieveOfEratosthenes(179424673, page_size=131072) # 11.5
    # primes = naiveSegmentedSieveOfEratosthenes(179424673, page_size=262144) # 11.2
    # primes = segmentedSieveOfEratosthenesOnOdds() # 1.99 seconds
    #primes = segmentedSieveOfEratosthenesOnOdds(179424673, page_size=16378) # 9.9
    # primes = segmentedSieveOfEratosthenesOnOdds(179424673, page_size=131072) # 6.8
    # primes = segmentedSieveOfEratosthenesOnOdds(179424673, page_size=262144) # 6.6
    primes = segmentedSieveOfEratosthenesOnOdds(10000000000, page_size=262144) # 6.6
    '''
    first_million_primes = np.load('/home/shawnghu/project_euler/utils/first_million_primes.npy')
    diprimes = {x: True for x in first_million_primes}
    for idx, p in enumerate(primes):
        if p not in diprimes:
            print(idx, p)
    pdb.set_trace()
    '''
    np.save('primes_up_to_10_digits', primes)


if __name__ == '__main__':
    main()
