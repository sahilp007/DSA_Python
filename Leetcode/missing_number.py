nums = [0, 1, 2, 4, 5, 6, 7]

a = 0
for i in range(len(nums)):
    a = a ^ nums[i]
    a = a ^ i

print(a ^ len(nums))
