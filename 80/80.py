from mpmath import mp

mp.dps = 150

# this one is weirdly easy? I have no idea why it has a 20% difficulty rating
s = 0
for i in range(1, 101):
    if i in [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]:
        continue
    s += sum(int(c) for c in str(mp.sqrt(i))[:101] if c != '.') # ignore the decimal point
print(s)
