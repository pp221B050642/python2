import numpy as np

# string = "417950030000000700060007000050009106800600000000003400900005000000430000200701580"
# matrix = [string[i:i+9] for i in range(0, len(string), 9)]
# matrix1 = np.asarray(matrix)
# # print(matrix1)
# matrix2 = []
# for i in matrix:
#     row = []
#     for j in i:
#         element = j
#         row.append(int(element))
#     matrix2.append(row)
# print(matrix2)


class Sudoku(str):
    def __init__(self, str):
        def string_to_matrix(s):
            divided = [s[i:i+9] for i in range(0, len(s), 9)]
            matrix = []
            for i in divided:
                row = []
                for j in i:
                    row.append(int(j))
                matrix.append(row)
            return np.asarray(matrix)
        self.string = str
        self.board = string_to_matrix(str)

    def get_row(self, n):
        for i in range(len(self.board)):
            if i == n:
                print(self.board[i])

    def get_column(self, m):
        column = self.board[0:9, m]
        print(column)
             
    def get_sqr(self, n, m):
        
        pass

game = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")
# print(game.board)
# game.get_row(0)
# game.get_column(8)
