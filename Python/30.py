class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        word_len = len(words[0])
        word_num = len(words)
        ans = []
        counter = Counter(words)

        for i in range(len(s) - word_len * word_num + 1):
            seen = {}
            idx = 0
            while idx < word_num:
                word = s[i + idx * word_len: i + idx * word_len + word_len]

                if word not in seen:
                    seen[word] = 0
                
                seen[word] += 1                
                if seen[word] > counter[word]:
                    break
                idx += 1

            if idx == word_num:
                ans.append(i)
        return ans
