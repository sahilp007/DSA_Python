try:
    test = int(input(""))
    for j in range(test):
        p = list(map(int, input().rstrip().split()))
        n, b, m = p[0], p[1], p[2]

        M = list(map(int, input().rstrip().split()))
        del M[:m]
        mf = []
        lf = M[:]
        count = 0
        n = 0
        for i in range(len(M)):
            if (i + 1) % 3 == 0:
                n += 3
            if M[i] in lf:
                print(count)
                exit()
            else:
                for k in range(b):
                    if M[i] % b == k:
                        lf = M[i + k:i + 2]
                elif M[i] % 3 == 2:
                    lf = M[i - 2:i + 1]
                else:
                    lf = M[i:i + 3]
                count += 1
                mf = lf
except:
    pass
