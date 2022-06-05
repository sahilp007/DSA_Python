def f(x):
    return x[0]


intervals = [[3, 10]]
newInterval = [4, 8]
intervals.append(newInterval)
l = sorted(intervals, key=f)

ans = []
c = l[0]
for i in range(len(l)):
    n = l[i]
    if n[0] <= c[1]:
        c[1] = max(c[1], n[1])
    else:
        ans.append(c)
        c = l[i]
n = c
if n[0] <= c[1]:
    c[1] = max(c[1], n[1])
    ans.append(c)
else:
    ans.append(c)
# return(ans)
print(ans)
