# y = x - d, z = x - 2d
# y^2 = x^2 - 2dx + d^2, z^2 = x^2 - 4dx + 4d^2
# x^2 - y^2 - z^2 = x^2 - (x^2 - 2dx + d^2) - (x^2 - 4d + 4d^2) = -x^2 + 6dx - 5d^2 = n
# in given example, x = 13, d = 3, n = 20: - 

x = 13
d = 3
n = 20
print(-(x ** 2) + 6 * d * x - 5 * d ** 2)

# y = x - 3d, -y^2 = -x^2 + 6dx - 9d^2
# -y^2 + 4d^2 = n
# i don't want to solve more diophantine equations