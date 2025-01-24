triangle_nums = []
x = 1
while True:
    triangle_nums.append(x * (x + 1) / 2)
    x += 1
    if (x * (x + 1) / 2) > (26 * 40):
        break

with open("words.txt", "r") as f:
    text = f.read()
    words = text.split(",")
    words = [word.strip('"') for word in words]

counter = 0
for word in words:
    triangle_score = sum(ord(x) - 64 for x in word)
    if triangle_score in triangle_nums:
        counter += 1

print(counter)
