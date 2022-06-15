class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n==0:
            return True
        flowerbed.append(0)
        prev=0
        for i in range(0,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[prev]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            if n==0:
                return True
            prev=i
            
        return False