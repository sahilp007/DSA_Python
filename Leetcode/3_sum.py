# # nums = [-2,0,1,1,2]
# # a = []
# #
# # for i in range(len(nums)):
# #     for j in range(i + 1, len(nums)):
# #         for k in range(j + 1, len(nums)):
# #             if nums[i] + nums[j] + nums[k] == 0:
# #                 # print("found", nums[i], nums[j], nums[k])
# #                 a.append([nums[i], nums[j], nums[k]])
# #
# # # a = list(dict.fromkeys(a))
# # ar = a
# # ar3=[ar[0]]
# # for i in range(len(ar)):
# #     for j in range(i, len(ar)):
# #         ar1 = sorted(ar[i])
# #         ar2 = sorted(ar[j])
# #         # print(ar1, ar2)
# #         if ar1!=ar2:
# #             ar3.append(ar[i])
# # # else:
# # #     ar3=ar
# # print(ar3)
# # # return(ar3)
# #
#
# def threeSum(nums):
#     # nums = [-1, 0, 1, 2, -1, -4]
#     res = []
#     nums.sort()
#
#     for i, a in enumerate(nums):
#         if i > 0 and a == nums[i - 1]:
#             continue
#
#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             threeSum = a + nums[l] + nums[r]
#             if threeSum > 0:
#                 r -= 1
#             elif threeSum < 0:
#                 l += 1
#             else:
#                 res.append([a, nums[1], nums[r]])
#                 l += 1
#                 while nums[l] == nums[l - 1] and l < r:
#                     l += 1
#     return (res)
#
# threeSum(nums = [-1,0,1,2,-1,-4])




import itertools
nums = [-1, 0, 1, 2, -1, -4]
result = []
nums.sort()
for lst in itertools.combinations(nums, 3):
    if sum(lst) == 0:
        result.append(lst)
unique_lst = []
[unique_lst.append(sublst) for sublst in result if not unique_lst.count(sublst)]
print(result)
print(unique_lst)