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
                counter = Counter([board[i*3 + k][j*3 + l] for k in range(3) for l in range(3)])
                for key, val in counter.items():
                    if key == ".":
                        continue
                    if val > 1:
                        return False
        
        return True
