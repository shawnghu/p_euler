from array import array

def extract_digits(num):
    # a = array('B')
    a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    while num > 0:
        digit = num % 10
        a[digit] += 1
        num //= 10
    return a

# print(extract_digits(162554))

for i in range(1000000, 1666667):
    digits = extract_digits(i)
    if i == 1428570:
        print(digits)
    candidate = True
    for x in range(2, 7):
        new_number = x * i
        if i == 1428570:
            print(new_number)
            print(extract_digits(new_number))
        if digits != extract_digits(new_number):
            candidate = False
            break
    if candidate:
        print(i)
        break
