with open('cipher.txt', 'r') as f:
    text = f.read().strip()
    nums = text.split(",")
    nums = [int(num) for num in nums]

'''
hist = {}
for num in nums:
    hist[num] = hist.get(num, 0) + 1
print(hist)
'''
print(nums)
def decrypt(password, ciphernums):
    out = ''
    # weird_character_counter = 0
    for idx, char in enumerate(ciphernums):
        dechar = chr(char ^ ord(password[idx % len(password)]))
        '''
        if not (('a' <= dechar and dechar <= 'z') or ('A' <= dechar and dechar <= 'Z') or ('0' <= dechar and dechar <= '9') or dechar == ' ' or dechar == "'" or dechar == '"'):
            # print(dechar)
            weird_character_counter += 1
            if weird_character_counter >= 15:
                return ''
        '''
        out += dechar
    if 'the' not in out:
        return ''
    print('made it here')
    return out
'''
with open('test.txt', 'w') as f:
    for i in range(97, 123): 
        for j in range(97, 123): 
            for k in range(97, 123): 
                password = chr(i) + chr(j) + chr(k)
                decrypted = decrypt(password, nums)
                if decrypted:
                    f.write(password + ": " + decrypted + '\n')
'''

decrypted = decrypt('exp', nums)
print(sum([ord(x) for x in decrypted]))



