# this one is simpler than it looks, in the following sense:
# if the sum of the digits needs to be a perfect square,
# then one digit needs to be a, and the remaining sum needs to be b, such that a^2 + b^2 = c^2
# well, the max value of a is 9, so the only valid triples are (3, 4, 5), (6, 8, 10), (5, 12, 13), (7, 24, 25), (8, 15, 17), (9, 40, 41)

# now we have to do some annoying combinatorics, i think. as an example, for (5, 12, 13), we have to decide both where 5 goes in a 20-digit number,
# as well as all the different ways to sum to 12
# of course, i don't think we really need to find all of them and compute their sum explicitly.

# first note that if the sum of all 20 digits is 12, the sum of all the digits in the last nine places can validly be anything from 0 to 12
# and also note that e.g, if the sum is 11, then there are 11 ways to place the last 1, which is annoying, because then we'll have to multiply by 11
# and if the sum is 10, then there are 11 ways to place a 2, and 55 ways to place a pair of 1s in the remaining 11 digits, so this is not great
# and this is not even factoring all the ways we can place the 5 in the 20 digits, although i think those might go away due to symmetry. 
