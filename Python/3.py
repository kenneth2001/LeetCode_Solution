class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_length = 0
        while end < len(s):
            if s[end] not in s[start:end]:
                end += 1
                max_length = max(max_length, end - start)
            else:
                start += 1
        return max_length