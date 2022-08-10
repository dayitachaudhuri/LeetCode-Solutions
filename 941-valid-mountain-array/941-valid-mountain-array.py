class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        change=0
        
        if len(arr)<3:
            return False
        
        if arr[0]>=arr[1]:
            return False
        
        for i in range(1,len(arr)-1):
            
            # If Equal
            if arr[i-1]==arr[i] or arr[i]==arr[i+1]:
                return False
            
            # Count Changes
            if (arr[i-1]>arr[i]) != (arr[i]>arr[i+1]):
                change+=1
            
            if change>1:
                return False
        
        # If there are zero increasing ot decreasing elements
        if change==1:
            return True
        
        return False
                