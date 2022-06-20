class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        
        def helper(board,r,col,posDiagonal,negDiagonal):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r+c) in posDiagonal or (r-c) in negDiagonal:
                    continue
                board[r][c]="Q"
                helper(board,r+1,col+[c],posDiagonal+[r+c],negDiagonal+[r-c])
                board[r][c]="."
                
        board=[["."]*n for i in range(n)]
        helper(board,0,[],[],[])
        return res