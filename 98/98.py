import pdb
import math
with open('words.txt', 'r') as f:
    words = f.read().strip().split(',')
    words = [word.strip('"') for word in words]

h = {}
pairs = []
for word in words:
    s = "".join(sorted(word))
    if s in h:
        pairs.append((word, h[s]))
    else:
        h[s] = word

pairs.sort(key=lambda x: len(x[0]), reverse=True)

squares = {}
squares_by_num_digit = [{} for x in range(10)]
x = 0
num_digits = 0
while True:
    sq = x ** 2
    if sq > 10 ** (num_digits):
        num_digits += 1
        if num_digits == 10: #we've established above that no word of longer than nine letters has an anagram in the set
            break
    squares[sq] = True
    squares_by_num_digit[num_digits][sq] = True
    x += 1

def try_square_substitution(word_pair, square_dict):
    word1, word2 = word_pair
    square_dict = square_dict[len(word1)]
    largest = 0
    for square in square_dict:
        # disqualify mappings that don't actually work
        mapping = {}
        numbers_used = {}
        dqd = False
        for (letter, number) in zip(word1, str(square)):
            if letter in mapping:
                if number != mapping[letter]:
                    dqd = True
                    break
                else:
                    continue
            if number in numbers_used:
                dqd = True
                break
            mapping[letter] = number
            numbers_used[number] = True
        if dqd:
            continue

        # try to apply the mapping to word 2 then
        anagram_square = 0
        '''
        for idx, char in enumerate(reversed(word2)):
            val = int(mapping[char])
            anagram_square += val * (10 ** idx)
        '''
        val = ''.join(mapping[char] for char in word2)
        val = int(val)
            
        if val in square_dict:
            val = max(square, val)
            if val > largest:
                largest = val
    return largest

largest = 0
for pair in pairs:
    val = try_square_substitution(pair, squares_by_num_digit)
    if val > largest:
        largest = val
print(largest)


'''
I've done the incorrect thing here. We need to actually keep track of what mapping we do from letters to numbers, sadly.
'''
pdb.set_trace()



