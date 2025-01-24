import itertools

def main():
    cubes = {}
    for i in range(1000000):
        key = tuple(sorted(str(i ** 3)))
        if key not in cubes:
            cubes[key] = [1, i ** 3]
        else:
            cubes[key][0] += 1
            if cubes[key][0] == 5:
                print(cubes[key])
                break

if __name__ == '__main__':
    main()
