nums = [1, 2, 3, 4, 5]

ans = [[]]

for num in nums:
    ans += [[num] + i for i in ans]
print(ans)
