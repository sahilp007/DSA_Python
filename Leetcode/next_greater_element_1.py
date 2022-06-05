a = [4, 1, 2]
b = [1, 3, 4, 2]
r = []

hel = dict(zip(b, range(len(b))))
for i in a:
    p = hel[i]
    flag = -1
    for j in b[p+1:]:
        if j>i:
            flag = j
            break
    r.append(flag)
print(r)
# return(r)
                    # noob akshay abhishek deepak shreyas imtesaal sahil

# a = sorted(nums1)
# b = sorted(nums2)
# i = 0
# k = 0
# for i in range(len(a)):
#     k=0
#     for j in range(len(b)):
#         c = a[i]+1
#         d = b[j]
#         if a[i] + 1 == b[j]:
#             r.append(b[j])
#             k+=1
#             break
#         elif a[i] + 2 == b[j]:
#             r.append(-1)
#             break
#     if k < 1:
#         r.append(-1)
