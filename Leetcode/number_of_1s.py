num = 10
res = 0
a = []
for i in range(num):
    res = 0
    n = int(bin(i)[2:])
    while n:
        res += n & 1
        n >>= 1
    a.append(res)
print(a)