
s = "3ssaasggsgrqww"
s1 = list(s)
test=[]
for char in s1:
    if test==[] or char != test[-1] :
        test.append(char)
    else:
        test.pop()
print("".join(test))
# return (test)