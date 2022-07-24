class Solution:
    def rob(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        dp={}
        def helper(i,j):
            if i>j:
                return 0
            if i in dp:
                return dp[i]
            val=max(arr[i] + helper(i+2,j), helper(i+1,j))
            dp[i]=val
            return val
        
        val1=helper(0,len(arr)-2)
        dp={}
        val2=helper(1,len(arr)-1)
        return max(val1,val2)
    
    '''   
        1 2 3 4 5 6 7
        |---|
    
    
    rob(i) = money + rob(i+2) , rob(i+1)
    
    '''  