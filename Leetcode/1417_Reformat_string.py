a = 'abc1234'
letters = ''
digits = ''
for i in range(len(a)):
    if a[i].isalpha():
        letters += a[i]
    if a[i].isdigit():
        digits += a[i]
if abs(len(letters)-len(digits))>1:
    print("exit")
l = 0
d = 0
ans = ''
while l < len(letters) and d< len(digits):
    ans += letters[l]
    l += 1
    ans += digits[d]
    d += 1
if len(letters) < len(digits):
    ans = digits[d] + ans
if len(letters) > len(digits):
    ans += letters[l]
print(ans)
