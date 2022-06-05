def comb(letter):
    combs = {'1': [""], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    if len(letter) == 1:
        res = combs[letter[0]]
        return res
    if len(letter)==0:
        res=[]
        return res
    res = combs[letter[0]]
    for k in letter[1:]:
        arr = []
        for i in res:
            for j in combs[k]:
                arr.append(i + j)
        res = arr
    return res


comb('3127')

# digits ='2365'
#
#
# def getChars(d):
#     if d == '2':
#         return ['a', 'b', 'c']
#     elif d == '3':
#         return ['d', 'e', 'f']
#     elif d == '4':
#         return ['g', 'h', 'i']
#     elif d == '5':
#         return ['j', 'k', 'l']
#     elif d == '6':
#         return ['m', 'n', 'o']
#     elif d == '7':
#         return ['p', 'q', 'r', 's']
#     elif d == '8':
#         return ['t', 'u', 'v']
#     elif d == '9':
#         return ['w', 'x', 'y', 'z']
#
#
# array = getChars(digits[0])
#
# if len(digits) == 1:
#     print(array)
# if len(digits) == 0:
#     print([])
#
# for d in digits[1:]:
#     chars = getChars(d)
#     newArray = []
#     for a in array:
#         for c in chars:
#             newArray.append(a + c)
#     array = newArray
# print (array)

