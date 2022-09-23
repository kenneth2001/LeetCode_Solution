class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        slen, plen = len(s), len(p)
        sidx, pidx = 0, 0
        staridx, tempidx = -1, -1

        while sidx < slen:
            # p[pidx] is ? or p[pidx] == s[sidx]
            if pidx < plen and (p[pidx] == '?' or s[sidx] == p[pidx]):
                sidx += 1
                pidx += 1
            # p[pidx] is *
            elif pidx < plen and p[pidx] == '*':
                staridx = pidx
                tempidx = sidx
                pidx += 1
            elif staridx == -1:
                return False
            # no match, but * exists
            else:
                pidx = staridx + 1
                sidx = tempidx + 1
                tempidx = sidx
        
        # check if all the remaining characters in p are *
        if not all([x == '*' for x in p[pidx:]]):
            return False
        return True
            

# Dynamic Programming Solution
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         m = len(s)
#         n = len(p)

#         # dp[i][j] = True if s[0..i-1] matches p[0..j-1]
#         dp = [[False] * (n + 1) for _ in range(m + 1)]
#         dp[0][0] = True

#         def check(i, j):
#             return (p[j] == '?' or p[j] == s[i])

#         # handle if the first character of p is *
#         for idx, char in enumerate(p):
#             if char == '*':
#                 dp[0][idx + 1] = dp[0][idx]
#             else:
#                 break
        
#         for i in range(m):
#             for j in range(n):
#                 if p[j] == '*':
#                     # dp[i + 1][j]: * matches empty string
#                     # dp[i][j + 1]: * matches one or more characters
#                     dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j]
#                 else:
#                     dp[i + 1][j + 1] = check(i, j) and dp[i][j]
        
#         return dp[m][n]
