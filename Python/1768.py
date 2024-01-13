class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        up_to = min(len(word1), len(word2))
        for idx in range(up_to):
            ans += word1[idx] + word2[idx]

        return ans + word1[up_to:] + word2[up_to:]