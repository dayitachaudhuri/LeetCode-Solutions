class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        m=len(flowerbed)
        i=0
        while i<m:
            if n==0:
                return True
            if i<m-1 and flowerbed[i+1]==1:
                i+=3
            elif flowerbed[i]==1:
                i+=2
            elif i>0 and flowerbed[i-1]==1:
                i+=1
            else:
                flowerbed[i]=1
                n-=1
                i+=2
        if n==0:
            return True
        return False