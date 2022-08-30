class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1'):
                    c=c+1
                    grid=Solution.cut(grid,i,j)
        return c
    def cut(grid,i,j):
        grid[i][j]='0'
        if(i+1<len(grid) and grid[i+1][j]=='1'):grid=Solution.cut(grid,i+1,j)    
        if(j+1<len(grid[0]) and grid[i][j+1]=='1'):grid=Solution.cut(grid,i,j+1)
        if(i-1>-1 and grid[i-1][j]=='1'):grid=Solution.cut(grid,i-1,j)
        if(j-1>-1 and grid[i][j-1]=='1'):grid=Solution.cut(grid,i,j-1)
        return grid