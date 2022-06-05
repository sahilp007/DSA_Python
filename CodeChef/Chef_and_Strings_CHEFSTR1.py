

try:
    t = int(input())
    for j in range(t):
        n=int(input())
        p = list(map(int, input().rstrip().split()))

        count = 0

        for i in range(len(p)-1):
            count += abs(p[i]-p[i+1])-1
            # print(abs(p[i]-p[i+1])-1)

        print(count)
except:
    pass