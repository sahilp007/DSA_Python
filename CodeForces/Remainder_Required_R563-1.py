
try:
    t=int(input())
    for j in range(t):

        p = list(map(int, input().rstrip().split()))
        x, y, n = p[0], p[1], p[2]
        r = n % x
        # print(r)
        if r > y:
            n = n - r + y
        elif r < y:
            n = n - (x - y + r)
        print(n)
except:
    pass
# p = list(map(int, input().rstrip().split()))
# x, y, n = p[0], p[1], p[2]
# r = n % x
# # print(r)
# if r > y:
#     n = n - r + y
# elif r < y:
#     n = n - (x - y + r)
# print(n)
