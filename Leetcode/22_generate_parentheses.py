'''
()(),(()),()()
()()(),(()()),((())),(())(),()(()),
'''

b = '()'
n = 3
arr2 = {'()'}


def main(arr):
    for j in arr:
        s1 = ['']

        res = j
        for i in range(len(res)):
            com = res[:i - 1] + b + res[i - 1:]
            s1.append(com)
        com = res + b
        s1.append(com)
        print(s1)
        return s1


for t in range(n):
    a = main(arr2)
    a = list(dict.fromkeys(a))
    arr2 = a

print(list(arr2))
a = list(arr2)
