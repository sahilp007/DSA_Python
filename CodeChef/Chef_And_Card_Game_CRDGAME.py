try:
    t = int(input())
    for j in range(t):
        n = int(input())
        chef = 0
        morty = 0
        for i in range(n):
            p = list(map(str, input().rstrip().split()))
            c, m = p[0], p[1]
            c = sum(map(int, c))
            m = sum(map(int, m))
            if c > m:
                chef += 1
            elif m > c:
                morty += 1
            else:
                morty += 1
                chef += 1
        if chef > morty:
            print(0, chef)
        elif chef < morty:
            print(1, morty)
        else:
            print(2, morty)
except:
    pass
