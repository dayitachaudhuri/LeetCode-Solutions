class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        rows=[1]*n
        cols=[1]*m
        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j]==0:
                    rows[i]=0
                    cols[j]=0
                    
        for i in range(0,n):
            for j in range(0,m):
                if rows[i]==0 or cols[j]==0:
                    matrix[i][j]=0