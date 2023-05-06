class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        return " ".join([sub[::-1] for sub in s])
