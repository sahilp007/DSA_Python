alphabet = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
ans=[]
for query in queries:
    count = 0
    small = 1111111111
    for i in query:
        if small > alphabet[i]:
            small = alphabet[i]
            letter = i
    fq = query.count(letter)
    letter = ''
    for word in words:
        small = 1111111111
        for i in word:
            if small > alphabet[i]:
                small = alphabet[i]
                letter = i
        fw = word.count(letter)
        if fq < fw:
            count += 1
    ans.append(count)
return(ans)