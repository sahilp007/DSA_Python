
try:
    t=int(input())
    for j in range(t):

        p = list(map(int, input().rstrip().split()))

        n,k=p[0],p[1]
        x=0
        a = list(map(int, input().rstrip().split()))
        count=0
        while True:
            count+=1
            for i in range(a):
                if (a[i]+x)%k==0:
                    a[i]+=x
                    x+=1
                else:
                    x+=1




except:
    pass