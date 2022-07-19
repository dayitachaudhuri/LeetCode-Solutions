class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        row=[1]
        
        for i in range(0,rowIndex):
            output=[1]
            for j in range(0,len(row)-1):
                output.append(row[j]+row[j+1])
            output.append(1)
            row=output
            
        return row