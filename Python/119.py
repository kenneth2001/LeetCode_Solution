class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]]
        for i in range(1, rowIndex+1):
            tmp = []
            for j in range(1+i):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(ans[i-1][j-1] + ans[i-1][j])
            ans.append(tmp)
        return ans[-1]
    