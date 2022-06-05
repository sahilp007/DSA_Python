import numpy as np

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
print(np.matrix(board))
word = "CF"

m = len(board)
n = len(board[0])
flag = True
for i in range(m):
    for j in range(n):
        if board[i][j] == word[0]:
            w = board
            k = 1
            a = i
            b = j
            while flag:
                if w[a + 0][b + 1] == word[k]:
                    w[a + 0][b + 1] = "1"
                    print(word[k])
                    k += 1
                    b = b + 1

                elif w[a + 1][b + 0] == word[k]:
                    w[a + 1][b + 0] = "1"
                    print(word[k])
                    k += 1
                    a = a + 1

                elif w[a - 1][b + 0] == word[k]:
                    w[a - 1][b + 0] = "1"
                    print(word[k])
                    k += 1
                    a = a - 1

                elif w[a + 0][b - 1] == word[k]:
                    w[a + 0][b - 1] = "1"
                    print(word[k])
                    k += 1
                    b = b - 1


                else:
                    flag = False
            if k == len(word):
                print("Done")
                exit()


    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.backtracking(i, j, word, board):
                    return True
        return False


    def backtracking(self, i, j, word, board):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False
        if board[i][j] == word[0]:
            board[i][j] = "~"
            if self.backtracking(i + 1, j, word[1:], board) or self.backtracking(i - 1, j, word[1:],
                                                                                 board) or self.backtracking(i, j + 1,
                                                                                                             word[1:],
                                                                                                             board) or self.backtracking(
                    i, j - 1, word[1:], board):
                return True
            board[i][j] = word[0]
        return False