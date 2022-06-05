s = "[{()(){}}(]]"
s.replace("()", "", 2)
# print(s)
while True:
    i=0
    try:
        k=0
        for i in range(len(s)):
            a = s[i] + s[i + 1]
            if a == "()" or a == "[]" or a == "{}":
                s = s[:i] + s[i+2:]
                k += 1
    except:
       pass
    if k < 1:
        break
# print(s)
if s!="":
    print("has")
    # return(False)
else:
    print("empty")
    # return(True)