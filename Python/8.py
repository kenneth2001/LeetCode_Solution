class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == '' or s == None: return 0

        sign = 1
        sol = 0

        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]
        
        for c in s:
            if c.isdigit():
                sol = sol * 10 + int(c)
            else:
                break
        
        sol = sol * sign
        if sol > 2147483647:
            return 2147483648
        elif sol < -2147483648:
            return -2147483648
        else:
            return sol
