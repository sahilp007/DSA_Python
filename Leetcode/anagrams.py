s = "anagram"
t = "nagaram"

s1 = list(s)
s2 = list(t)

s1.sort()
s2.sort()
print(s1, s2)
if (s1 == s2):
    print(True)
