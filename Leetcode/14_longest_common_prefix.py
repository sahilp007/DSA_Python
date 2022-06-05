st = ["ab", "a"]
pf = st[0]
for i in range(len(st)):
    # print(st[i])
    rem = ''
    for j in range(min(len(pf), len(st[i]))):
        # print(st[i][:j])
        if st[i][j] == pf[j]:
            rem += pf[j]
        else:
            pf = rem
            break
            # print(pf)
    pf = rem
print(pf)
