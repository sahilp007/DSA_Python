try:
    t = int(input())
    for j in range(t):
        p = list(map(int, input().rstrip().split()))

        v, c, n, m = p[0], p[1], p[2], p[3]
        if n + m == 0:
            print("No")
            exit()

        nl = []
        ml = []
        for i in range(n):
            nl.append(n)
        for i in range(m):
            ml.append(m)
        h=False
        print(nl,ml)
        nm = nl+ml
        mn = ml+(nl)
        print(nm, mn)
        for i in range(len(nm)):

            print(i,v,c)
            if nm[i] == n and v >= c:
                v -= 1
            else:
                c -= 1
            print(i, v, c)
            if nm[i] == m and v >= c:
                c -= 1
            else:
                v -= 1
            print(i, v, c)
            # if v < 0 or c < 0:
            #     continue
            print(i,v,c)
            if i == len(nm):
                print("Yes")
                h=True
                exit()

        v, c, n, m = p[0], p[1], p[2], p[3]

        for i in range(len(mn)):
            print(i,v,c)
            if nm[i] == n and v >= c:
                v -= 1
            else:
                c -= 1

            print(i,v,c)
            if nm[i] == m and v >= c:
                c -= 1
            else:
                v -= 1

            print(i,v,c)
            # if v < 0 or c < 0:
            #     continue
            print(i,v,c)
            if i == len(nm):
                print("Yes")
                h=True
                exit()
        if not h:
            print("No")


except:
    pass
