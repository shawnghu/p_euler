# Look at the number of different values mod N
def find_num_values(fn, modn):
    s = set()
    for i in range(modn):
        s.add(fn(i) % modn)
    return (s)
    # return len(s)
        
results = {}
# for x in [4, 16, 64, 256]:
#     results[x] = find_num_values(lambda y: y**2, x)
print(results)
values = (find_num_values(lambda y: y**2, 256))
counter = 0
for x in values:
    for y in values:
        if x + y in values:
            counter += 1
            print (x, y, x + y)
print(counter)
