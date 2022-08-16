class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = {}
        
        for c in s:
            if c not in cnt:
                cnt[c] = 1
            else:
                cnt[c] += 1
                
        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
            
        return -1