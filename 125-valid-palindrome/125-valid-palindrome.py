class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[x.lower() for x in list(s) if x.isalnum()]
        for i in range(len(arr)//2):
            if arr[i]!=arr[len(arr)-i-1]:
                return False
        return True