class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom={}
        mag={}
        for i in ransomNote:
            if i in ransom:
                ransom[i]+=1
            else:
                ransom[i]=1
        for i in magazine:
            if i in ransom:
                if i in mag:
                    mag[i]+=1
                else:
                    mag[i]=1
        for i in ransom:
            if i not in mag or mag[i]<ransom[i]:
                return False
        return True