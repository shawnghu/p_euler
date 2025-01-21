# the rules aren't very complicated and don't interact with each other in any important ways
# also there are really no special cases, you just have to handle the groups of five first before subtractive rules
# and string replace already does exactly what you want in all cases, so this function looks very simple
def compute_saved_chars(roman):
    total = 0
    while True:
        if 'IIIII' in roman:
            total += 4
            roman = roman.replace('IIIII', 'V')
        elif 'XXXXX' in roman:
            total += 4
            roman = roman.replace('XXXXX', 'L')
        elif 'CCCCC' in roman:
            total += 4
            roman = roman.replace('CCCCC', 'D')
        elif 'VIIII' in roman:
            total += 3
            roman = roman.replace('VIIII', 'IX')
        elif 'LXXXX' in roman:
            total += 3
            roman = roman.replace('LXXXX', 'XC')
        elif 'DCCCC' in roman:
            total += 3
            roman = roman.replace('DCCCC', 'CM')
        elif 'IIII' in roman:
            total += 2
            roman = roman.replace('IIII', 'IV')
        elif 'XXXX' in roman:
            total += 2
            roman = roman.replace('XXXX', 'XL')
        elif 'CCCC' in roman:
            total += 2
            roman = roman.replace('CCCC', 'CD')
        elif 'VIIII' in roman:
            total += 3
            roman = roman.replace('VIIII', 'IX')
        elif 'LXXXX' in roman:
            total += 3
            roman = roman.replace('LXXXX', 'XC')
        elif 'DCCCC' in roman:
            total += 3
            roman = roman.replace('DCCCC', 'CM')
        else:
            break
    return roman, total


with open('89/0089_roman.txt', 'r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    roman, saved = compute_saved_chars(line)
    total += saved
    print(line, roman)

print(total)
