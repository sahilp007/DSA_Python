# # import math
# # l=0
# # n = 3
# # temp = head
# # while head:
# #     l+=1
# #     head = head.next
# #
# # find = l-n-1
# # head = temp
# # while find:
# #     head = head.next
# # head = head.next.next
# #
# h, b = 1123, 1
# a = h*(b+0)
# a = '{:.2f}'.format(round(a, 2))
# print(a)
#
# try:
#     t = int(input())
#     for j in range(t):
#         p = list(map(int, input().rstrip().split()))
#
#         h, b = p[0], p[1]
#         a = h(b)
#         a = '{:.2f}'.format(round(a, 2))
#         print(a)
#
#
# except:
#     pass


def nextfit(grp, cab):
    res = 0
    rem = cab
    for i in range(len(grp)):
        if rem >= grp[i]:
            rem = rem - grp[i]
        else:
            res += 1
            rem = cab - grp[i]
    return res
try:
    t = int(input())
    for j in range(t):
        p = list(map(int, input().rstrip().split()))
        cab = 4
        print(nextfit(p, cab))

except:
    pass