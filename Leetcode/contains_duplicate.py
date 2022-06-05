nums = [1, 2, 3, 1]

nums.sort()
r= False
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
        r = True
# return r

# for i in range(len(nums)):
#     if nums[i] in nums[i + 1:len(nums)]:
#         r = True
#         break
