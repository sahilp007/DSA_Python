s1 = 'this is not acceptable'
s2 = 'this will not be acceptable'
s3 = {}
ans = []
for i in s1.split():
    if i in s3:
        s3[i] += 1
    else:
        s3[i] = 1

for i in s2.split():
    if i in s3:
        s3[i] += 1
    else:
        s3[i] = 1

for i in s3:
    if s3[i] == 1:
        ans.append(i)
