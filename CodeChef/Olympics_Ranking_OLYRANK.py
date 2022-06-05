try:
    t = int(input())
    for j in range(t):
        points = list(map(int, input().rstrip().split()))

        sum1 = sum(points[:3])
        sum2 = sum(points[3:])

        if sum1 > sum2:W
            rank = 1
        else:
            rank = 2

        print(rank)

except:
    pass
