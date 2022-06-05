import numpy as np
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
# print(np.matrix(mat))
n = len(mat)
for i in range(n // 2):
    mat[i], mat[n - i - 1] = mat[n - i - 1], mat[i]
# print(np.matrix(mat))


for i in range(n):
    for j in range(i,n):
        mat[i][j] , mat[j][i] = mat[j][i], mat[i][j]
# print(np.matrix(mat))
