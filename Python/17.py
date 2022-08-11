class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        table = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans = []

        def search(i, path):
            if i == len(digits):
                ans.append(''.join(path))
                return

            for letter in table[digits[i]]:
                path.append(letter)
                search(i + 1, path)
                path.pop()

        search(0, [])
        return ans
