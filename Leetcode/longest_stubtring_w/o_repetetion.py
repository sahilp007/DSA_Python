s = "abcdecddi"
m = 0
cset = set()

left = 0
right = 0

for i in range(len(s)):
    print(cset, s[i])
    if s[i] not in cset:
        right += 1
        print(cset)
        cset.add(s[i])
    else:
        print(cset)
        for j in range(left, right):
            print(cset, s[j])
            left += 1
            if s[i] == s[j]:
                cset.remove(s[j])
                break
            else:
                print(cset)
                cset.remove(s[j])
        cset.add(s[i])
print(cset)
seen = ''
mx = 0
for c in s:
    if c not in seen:
        seen += c
    else:
        seen = seen[seen.index(c) + 1:] + c
    mx = max(mx, len(seen))
