class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        if len(grid)==0 or len(grid[0])==0:
            return 0
        for i in range(0,len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j]<0:
                    count+=len(grid[0])-j
                    break
        return count