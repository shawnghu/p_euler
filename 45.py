triangular = []
pent = []
hexag = []
for n in range(1, 100000):
    triangular.append(n * (n + 1) / 2)
    pent.append(n * (3 * n - 1) / 2)
    hexag.append(n * (2 * n - 1))

dipent = {x: True for x in pent}
dihex = {x: True for x in hexag}

for trinum in triangular:
    if trinum in dipent and trinum in dihex:
        print(trinum)
