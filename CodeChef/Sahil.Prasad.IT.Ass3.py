# # # # # # # SNDMAX
# # # # # # try:
# # # # # #     t = int(input())
# # # # # #     for j in range(t):
# # # # # #         p = list(map(int, input().rstrip().split()))
# # # # # #         p.sort()
# # # # # #         print(p[1])
# # # # # #
# # # # # #
# # # # # #
# # # # # # except:
# # # # # #     pass
# # # # #
# # # # # # MAXTHREE
# # # # # try:
# # # # #     t = int(input())
# # # # #     for j in range(t):
# # # # #         p = list(map(int, input().rstrip().split()))
# # # # #         p.sort()
# # # # #         print(p[2])
# # # # #
# # # # # except:
# # # # #     pass
# # # #
# # # # #SQUNUM
# # # #
# # # # try:
# # # #     t = int(input())
# # # #     for j in range(t):
# # # #         n=int(input())
# # # #         print(n**2)
# # # #
# # # # except:
# # # #     pass
# # #
# # # # TEST
# # # try:
# # #     while True:
# # #         n = int(input())
# # #         if n == 42:
# # #             break
# # #         print(n)
# # #
# # # except:
# # #     pass
# #
# # # INTRN020
# # from math import sqrt
# # Max = 1000005
# # isPrime = []
# # primes = [2]
# # for i in range(Max):
# #     isPrime.append(True)
# #
# # for (p) in range(2, int(sqrt(Max))):
# #     if isPrime[p]:
# #         for i in range(p * p, Max, p):
# #             isPrime[i] = False
# # for p in range(2, Max):
# #     if isPrime[p]:
# #         primes.append(p)
# #
# # n = int(input())
# # for a in range(1,n+1):
# #     print(primes[a])
#
# #INTRN004
# try:
#     t = int(input())
#     for j in range(t):
#         n = int(input())
#         print(int(bin(n)[2:]))
#
# except:
#     pass

# # INTRN006
# try:
#     t = int(input())
#     for j in range(t):
#         n = int(input())
#         sum = 0
#         for x in range(1, n):
#             if n % x == 0:
#                 sum += x
#         if sum == n:
#             print("YES")
#         else:
#             print("NO")
# except:
#     pass

# cook your dish here

# # INTRN006
# try:
#     t = int(input())
#     while t > 0:
#         n = int(input())
#         if n < 2:
#             print("NO")
#             exit()
#         i = 2
#         sum1 = 0
#         while i * i <= n:
#             if n % i == 0:
#                 if i * i != n:
#                     sum1 += i
#                     sum1 += (n // i)
#                 else:
#                     sum1 += i
#             i += 1
#         sum1 += 1
#         if sum1 == n:
#             print("YES")
#         else:
#             print("NO")
#         t = t - 1
# except:
#     pass

try:
    a = []
    t = int(input())
    for y in range(0, 20):
        x = (2 ** (y - 1)) * (2 ** y - 1)
        a.append(x)

    for j in range(t):
        n = int(input())
        if n < 2:
            print("NO")
            continue
        if n in a:
            print("YES")
        else:
            print("NO")

except:
    pass
