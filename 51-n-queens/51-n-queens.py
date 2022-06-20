class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        col=[]
        posDiagonal=[]
        negDiagonal=[]
        board=[["."]*n for i in range(n)]
        
        def helper(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r+c) in posDiagonal or (r-c) in negDiagonal:
                    continue
                    
                col.append(c)
                posDiagonal.append(r+c)
                negDiagonal.append(r-c)
                board[r][c]="Q"
                
                helper(r+1)
                
                col.pop()
                posDiagonal.pop()
                negDiagonal.pop()
                board[r][c]="."
                
        helper(0)
        return res