# for MODULUS in [32, 64, 128, 144, 192, 256, 512, 1024, 2048, 4096, 8192]:
# for MODULUS in range(3, 200):
for MODULUS in [9 * 25 * 49 * 121 * 13]:
    squares = set()
    for i in range(MODULUS):
        squares.add((i * i) % MODULUS)


    potentials = set()
    for i in range(MODULUS):
        # if (3 * i * i + 4 * i + 1) % MODULUS in squares:
        #    potentials.add(i)
        if (3 * i * i + 4 * i + 1) % MODULUS in squares:
            potentials.add(i)

    print(MODULUS, len(potentials) / MODULUS)
        
