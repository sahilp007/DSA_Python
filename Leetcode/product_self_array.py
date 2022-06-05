nums = [1,2,3,4]
mul = 1
k = 0
for i in nums:
    if i == 0:
        k += 1
        continue
    else:
        mul *= i
# print(mul)

if k > 1:
    num = [0] * len(nums)


elif k == 1:
    num = [0] * len(nums)
    for i in range(len(nums)):
        if nums[i] == 0:
            num[i] = mul

else:
    num = [0] * len(nums)
    for i in range(len(nums)):
        num[i] = (mul // nums[i])

print(num)
