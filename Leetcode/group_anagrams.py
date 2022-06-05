strs = [""]

o = {}
for word in strs:
    w = "".join(sorted(word))
    if w not in o:
        o[w] = [word]
    else:
        o[w].append(word)

print(list(o.values()))



