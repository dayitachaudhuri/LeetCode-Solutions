class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ans=[]
        columns=[]
        posDiag,negDiag=[],[]
        board=[["."]*n for i in range(0,n)]
        
        def helper(row):
            if row==n:
                sol=["".join(r) for r in board]
                ans.append(sol)
            
            for col in range(0,n):
                if col not in columns and (row+col) not in posDiag and (row-col) not in negDiag:
                    
                    board[row][col]="Q"
                    columns.append(col)
                    posDiag.append(row+col)
                    negDiag.append(row-col)
                
                    helper(row+1)
                
                    board[row][col]="."
                    columns.pop()
                    posDiag.pop()
                    negDiag.pop()
                
        helper(0)
        return ans