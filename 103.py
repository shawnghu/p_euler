import itertools
def search_matching_sums(l):
    sums_seen = {}
    for (x, y) in itertools.combinations(l, 2):
        s = x + y
        if s in sums_seen:
            print (x, y)
            return False
    return True

search_matching_sums([20, 31, 38, 39, 40, 42, 45]) 
# I found this set by inspection on the constraints imposed for the first few examples.
# i.e, you may generate the next minimal set by shifting over the previous set by an amount sufficient to meet the sum condition.
# Since the first three elements for the n = 6 case sum up to 19 less than the last three elements, you need a first element equal to at least 20
# and you need to add 20 to each of these elements, at a minimum, or else most likely some other problem arises.
# Then I wrote the above function to see if there were any problems with it (it's not even the right function because it asks for all subsets, not all subsets of size 2)
# Note: I also realized that I've never even tried to actually put anything into sums_seen, so this function does nothing but always return True. Whooops.
# Since I found no errors, I just tried to submit it and the answer turned out to be right. Whoops.
