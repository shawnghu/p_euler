
MAX_COORD = 50

# many symmetries to take advantage of
# but this really should be small enough to brute force
count = 0
for x1 in range(MAX_COORD + 1):
    for y1 in range(MAX_COORD + 1):
        for x2 in range(MAX_COORD + 1):
            for y2 in range(MAX_COORD + 1):
                if x1 == x2 and y1 == y2:
                    continue
                if x1 == 0 and y1 == 0:
                    continue
                if x2 == 0 and y2 == 0:
                    continue
                # find all three rays, take pairwise dot products; if one is zero it's a right triangle
                ray1 = (x1, y1)
                ray2 = (x2, y2)
                ray3 = (x2 - x1, y2 - y1)
                if abs(ray1[0] * ray3[0] + ray1[1] * ray3[1]) < 1e-6:
                    count += 1
                    continue
                if abs(ray2[0] * ray3[0] + ray2[1] * ray3[1]) < 1e-6:
                    count += 1
                    continue
                if abs(ray1[0] * ray2[0] + ray1[1] * ray2[1]) < 1e-6:
                    count += 1
                    continue
print(count // 2) # since we could flip the points, we counted each right triangle twice
