try:
    t = int(input())
    for j in range(t):
        n = int(input())
        p = list(map(int, input().rstrip().split()))
        x = (n - 1) / 2
        i = 0
        po = x + 1
        s = 0
        while po > x:
            po = 0
            for k in range(len(p) - 1):
                if p[k + 1] - p[k] >= 0:
                    po += 1
                    print("po", p[k + 1], p[k], p[k + 1] - p[k])

                p[i] = -p[i]
                print(p[i], "po=", po)
                print(p)
            i += 1
            if s % (n - 1) == 0:
                i = 0
            s += 1
        print(p)


except:
    pass
