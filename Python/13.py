class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        sol = 0
        while len(s) != 0:
            if len(s) and s[:2] in table.keys():
                sol += table[s[:2]]
                s = s[2:]
            else:
                sol += table[s[0]]
                s = s[1:]
        return sol