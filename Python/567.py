from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])

        if s1_counter == s2_counter:
            return True
    
        for i in range(s1_len, len(s2)):
            curr_char = s2[i]
            s2_counter[s2[i-s1_len]] -= 1
            s2_counter[curr_char] += 1

            if s2_counter[curr_char] == s1_counter[curr_char]:
                if s1_counter == s2_counter:
                    return True

        return False
