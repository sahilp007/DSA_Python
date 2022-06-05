try:
    t = int(input())
    for j in range(t):
        length = int(input())
        n = list(map(int, input().rstrip().split()))

        s = dict()
        p = dict()
        b = -1
        for i in range(len(n)):
            if n[i] not in s:
                s[n[i]] = 1
                p[n[i]] = i
            else:
                s[n[i]] += 1
            if s[n[i]] > 1:
                b = n[i]
                break
            print(i)

except:
    pass
