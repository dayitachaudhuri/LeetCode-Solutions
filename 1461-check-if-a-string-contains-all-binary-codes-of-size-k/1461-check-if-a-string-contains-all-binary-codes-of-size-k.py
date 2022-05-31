class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        us = set();
        for i in range(0,len(s)-k+1):
            us.add(s[i:i+k])
        if len(us)==2**k:
            return True
        else:
            return False