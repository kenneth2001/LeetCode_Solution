class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            counter = Counter(board[i])
            for key, val in counter.items():
                if key == ".":
                    continue
                if val > 1:
                    return False

        for i in range(9):
            counter = Counter([board[j][i] for j in range(9)])
            for key, val in counter.items():
                if key == ".":
                    continue
                if val > 1:
                    return False

        for i in range(3):
            for j in range(3):
                counter = Counter([board[i*3 + k][j*3 + l]
                                  for k in range(3) for l in range(3)])
                for key, val in counter.items():
                    if key == ".":
                        continue
                    if val > 1:
                        return False

        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # store the value occur in each row, col, and box
        row_occur = []
        for i in range(9):
            occur = set()
            for j in range(9):
                if board[i][j] != ".":
                    occur.add(board[i][j])
            row_occur.append(occur)

        col_occur = []
        for i in range(9):
            occur = set()
            for j in range(9):
                if board[j][i] != ".":
                    occur.add(board[j][i])
            col_occur.append(occur)

        box_occur = []
        for i in range(3):
            for j in range(3):
                occur = set()
                for k in range(3):
                    for l in range(3):
                        if board[i*3 + k][j*3 + l] != ".":
                            occur.add(board[i*3 + k][j*3 + l])
                box_occur.append(occur)

        def dfs(i, j):
            if i == 9:
                return True
            if j == 9:
                return dfs(i + 1, 0)
            if board[i][j] != ".":
                return dfs(i, j + 1)

            for val in "123456789":
                if val in row_occur[i] or val in col_occur[j] or val in box_occur[i//3*3 + j//3]:
                    continue
                board[i][j] = val
                row_occur[i].add(val)
                col_occur[j].add(val)
                box_occur[i//3*3 + j//3].add(val)
                if dfs(i, j + 1):
                    return True
                else:
                    board[i][j] = "."
                    row_occur[i].remove(val)
                    col_occur[j].remove(val)
                    box_occur[i//3*3 + j//3].remove(val)

            return False

        dfs(0, 0)
