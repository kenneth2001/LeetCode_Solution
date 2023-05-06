class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def solver(path, n, k):
            if k == 0: 
                ans.append(path)
                return
            
            x = path[-1] if path else 0
            for j in range(x+1, n-k+2):
                solver(path+[j], n, k-1)
            
        solver([], n, k)
        return ans

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         ans = []

#         def solver(start, path):
#             if len(path) == k:
#                 ans.append(path)
#                 return

#             for i in range(start, n+1):
#                 solver(i+1, path+[i])

#         solver(1, [])
#         return ans
