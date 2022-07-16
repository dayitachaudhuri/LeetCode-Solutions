class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp={}
        def helper(i,j,moves):
            if i<0 or j<0 or i>=m or j>=n:
                return 1
            if moves<=0:
                return 0
            if (i,j,moves) in dp:
                return dp[(i,j,moves)]
            dp[(i,j,moves)]=(helper(i+1,j,moves-1)+helper(i,j+1,moves-1)+helper(i-1,j,moves-1)+helper(i,j-1,moves-1))%(10**9+7)
            return dp[(i,j,moves)]
        return helper(startRow,startColumn,maxMove)