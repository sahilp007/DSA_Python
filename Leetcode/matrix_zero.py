mat = [[1, 2, 3],
       [0, 5, 6],
       [7, 8, 9],
       [13, 14, 0]]

m, n = set(), set()

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 0:
            m.add(i)
            n.add(j)

for i in range(len(mat)):
    if i in m:
        for j in range(len(mat[0])):
            mat[i][j] = 0

for i in range(len(mat[0])):
    if i in n:
        for j in range(len(mat)):
            mat[j][i] = 0
print(mat)
