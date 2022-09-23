class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matching = {}

        for s in strs:
            key = "".join(sorted(s))
            if key in matching:
                matching[key].append(s)
            else:
                matching[key] = [s]
        
        return list(matching.values())
