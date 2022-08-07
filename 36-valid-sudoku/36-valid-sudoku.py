class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        items = {}
        
        for row in board:
            for item in row:
                if item == ".":
                    continue
                if item in items:
                    return False
                items[item] = 1
            items.clear()
                
        for col in range(n):
            for row in range(n):
                if board[row][col] == '.': 
                    continue
                if board[row][col] in items:
                    return False
                else:
                    items[board[row][col]] = 1            
            items.clear()
            
        for i in range(3):
            for j in range(3):
                row = i * 3
                col = j * 3
                for r in range (row, row+3):
                    for c in range (col, col+3):
                        if board[r][c] == '.': 
                            continue
                        if board[r][c] in items:
                            return False
                        else:
                            items[board[r][c]] = 1       
                items.clear()
                
        return True
                