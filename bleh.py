# # n = 6
# # for i in range(n):
# #     print('x' * i)
# #
# # for i in range(n, 0, -1):
# #     print('x' * i)
# #
# # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# # for i in range(n):
# #     for k in range(i, n - 1):
# #         print(' ', end='')
# #     for j in range(i, 0, -1):
# #         print('x ', end='')
# #     print("")
# # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# # for i in range(n):
# #     for k in range(i, n - 1):
# #         print(' ', end='')
# #     for j in range(i, 0, -1):
# #         print('x', end='')
# #     print("")
# # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# #
# # a = [1, 1, 2, 3, 3, 3, 3, 4]
# #
# # b = list(dict.fromkeys(a))
# # final = []
# # for i in range(len(a) - 1):
# #     if a[i] != a[i + 1]:
# #         final.append(a[i])
# # final += [a[-1]]
# # print(final)
# #
#
# a=()
# a.add(7)
# print(a)
#

# s = "adbc"
# t = "e r i c h r o t"
t = ""
s = input()
k = int(input())
# k = 2
while s:
    if s == "" or len(s) == 1:
        print(s)
        break
    ch = "z1"
    for i in range(min(k, len(s))):
        if ch > s[i]:
            ch = s[i]
    t += ch
    # print(s.replace(ch, ""))
    s = s.replace(ch, "", 1)
print(t)