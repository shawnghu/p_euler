def is_increasing(num):
    s = str(num)
    last = s[0]
    for char in s[1:]:
        if char < last:
            return False
        last = char
    return True


def is_decreasing(num):
    s = str(num)
    last = s[0]
    for char in s[1:]:
        if char > last:
            return False
        last = char
    return True

def is_bouncy(num):
    return not is_increasing(num) and not is_decreasing(num)

# print(is_increasing(134468))
# print(is_bouncy(134468))
# print(is_bouncy(155349))

non_bouncy_count = 0
bouncy_count = 0

for i in range(1, 100000000):
    if i % 50000 == 0:
        print(i)
    if is_bouncy(i):
        bouncy_count += 1
    else:
        non_bouncy_count += 1
    if bouncy_count == 99 * non_bouncy_count:
        print(i)
        sys.exit()

