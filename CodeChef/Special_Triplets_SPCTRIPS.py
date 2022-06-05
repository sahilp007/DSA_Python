nums = [1, 2, 3, 4, 5, 6, 7]
ans = []
d = 2

for i in range(d, len(nums)):
    ans.append(nums[i])
for i in range(0, d):
    ans.append(nums[i])

ans2 = nums[d:] + nums[:d]

# for(int i=d;i<lenth(nums);i++){
# ans[i-d]=nums[i]
# }
# for(int i=0;i<d;i++){
# ans[lenght(nums)-d]=nums[i]
# }