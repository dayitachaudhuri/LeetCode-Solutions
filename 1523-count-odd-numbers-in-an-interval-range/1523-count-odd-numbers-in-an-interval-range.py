class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2!=0:
            num=((high-low)//2)+1
        else:
            num=(high-low+1)//2
        return num