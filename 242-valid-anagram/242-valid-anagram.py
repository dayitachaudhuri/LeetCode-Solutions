class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cacheS={}
        for i in s:
            if i in cacheS:
                cacheS[i]+=1
            else:
                cacheS[i]=1
        cacheT={}
        for i in t:
            if i in cacheT:
                cacheT[i]+=1
            else:
                cacheT[i]=1     
        
        if cacheS==cacheT:
            return True
        return False