class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        if numRows>=2:
            ans.append([1,1])
        for i in range(0,numRows-2):
            temp=[1]
            for j in range(0,i+1):
                temp.append(ans[-1][j]+ans[-1][j+1])
            temp.append(1)
            ans.append(temp)
        return ans