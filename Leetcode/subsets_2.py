nums = [1, 2, 2]

ans = [[]]
for num in nums:
    ans += [[num] + i for i in ans]
print(ans)
res = list(set(tuple(sorted(sub)) for sub in ans))
ans = []
for r in res:
    ans.append(list(r))
