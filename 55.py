def reverse(num):
    return int(str(num)[::-1])

def is_palindromic(num):
    a = str(num)
    return a == a[::-1]

def test_lychrel(num):
    for i in range(50):
        num += reverse(num)
        if is_palindromic(num):
            return False
    return True

counter = 0
for i in range(10000):
    if test_lychrel(i):
        counter += 1
print(counter)
