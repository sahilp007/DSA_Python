try:
    test = int(input(""))

    for j in range(test):

        p = list(map(int, input().rstrip().split()))
        m = p[0]
        n = p[1]

        a = list(map(int, input().rstrip().split()))
        b = []
        for i in range(max(a)):
            b.append(False)
            # print(b[i])

        for i in a:
            # print(b[i - 1], i - 1)
            b[i - 1] = True
        count = 0
        miss = []
        for i in range(n):
            if not b[i]:
                miss.append(i + 1)
                count += 1
        if count < 1:
            print(-1)
        else:
            print(max(miss))
except:
    pass
