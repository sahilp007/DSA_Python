import pprint


def floodFill(mat, r, c, toF, prevF):
    if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]):
        return
    if mat[r][c] != prevF:
        return

    mat[r][c] = toF
    floodFill(mat, r + 1, c, toF, prevF)
    floodFill(mat, r, c + 1, toF, prevF)
    floodFill(mat, r - 1, c, toF, prevF)
    floodFill(mat, r, c - 1, toF, prevF)


mat = [["1", "1", "1", "2", "1", "1", "1"],
       ["2", "2", "1", "2", "2", "1", "1"],
       ["0", "2", "2", "2", "1", "1", "1"],
       ["1", "1", "0", "2", "1", "2", "2"],
       ["1", "1", "2", "2", "1", "0", "0"]]

floodFill(mat, 1, 3, "-", "2")

pprint.pprint(mat)
