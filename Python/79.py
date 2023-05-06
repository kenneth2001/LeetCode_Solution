class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)
        path = set()

        def dfs(i, j, word_idx):
            if i < 0 or i == m or j < 0 or j == n or board[i][j] != word[word_idx] or (i, j) in path:
                return False
            
            if word_idx == word_len - 1:
                return True
            
            path.add((i, j))
            res = dfs(i + 1, j, word_idx + 1) or dfs(i - 1, j, word_idx + 1) or dfs(i, j + 1, word_idx + 1) or dfs(i, j - 1, word_idx + 1)
            path.remove((i, j))
            return res
        
        counter = Counter([board[i][j] for i in range(m) for j in range(n)])

        # if the first letter of the word appears more times than the last letter, reverse the word
        if counter[word[0]] > counter[word[-1]]:
            word = word[::-1]

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
        