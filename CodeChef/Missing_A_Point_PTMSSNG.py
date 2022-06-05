#
# # try:
# t=int(input())
# for j in range(t):
#     n=int(input())
#     x=[]
#     y=[]
#     for i in range(4*n-1):
#         p = list(map(int, input().rstrip().split()))
#
#         x.append(p[0])
#         y.append(p[1])
#     i=0
#     print(x,y)
#     while len(x)/2 > 0.5:
#         print(len(x)/2,x[i])
#         tx=x.index(x[i])
#         x.pop(tx)
#         x.pop(tx)
#         print(tx+1)
#         i+=1
#         print(x,tx)
#     i = 0
#     print("y")
#     while len(y) / 2 > 0.5:
#         ty = y.index(y[i])
#         print(ty)
#         y.remove(y.index(ty))
#         y.remove(y.index(ty))
#         i += 1
#         print(y)
# # except:
# #     pass
try:
    X = -11111
    Y = -11111
    t = int(input())
    for j in range(t):
        n = int(input())
        x = []
        y = []
        for i in range(4 * n - 1):
            p = list(map(int, input().rstrip().split()))

            x.append(p[0])
            y.append(p[1])
        i = 0
        # print(x,y)
        while len(x) / 2 > 0.5:
            # print(len(x)/2,x[i])

            tx = x.index(x[i])
            ttx = x[i]
            try:
                x.remove(ttx)
                x.remove(ttx)
            except:
                X = ttx
                # print("X=",X)
                break
            # print("ttx=",ttx)
            i += 1
            # print(x)
        else:
            X = x[0]
        i = 0
        # print("y")
        while len(y) / 2 > 0.5:
            ty = y.index(y[i])
            tty = y[i]
            try:
                y.remove(tty)
                y.remove(tty)
            except:
                Y = tty
                break
                # print("Y=",Y)
            # print("tty=",tty)
            i += 1
            # print("y=",y)
        else:
            Y = y[0]

    print(X, Y)
except:
    pass
