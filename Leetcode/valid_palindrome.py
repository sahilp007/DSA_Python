import re

s = s.lower()
r = ""
li = list(re.findall(r"[A-Za-z0-9]", s))
for i in li:
    r += i
r1 = r[::-1]
if r == r1:
    return (True)
else:
    return(False)