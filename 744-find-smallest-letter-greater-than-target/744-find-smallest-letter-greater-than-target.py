class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        val=letters[0]
        for l in letters:
            if l>target:
                val=l
                break
        return val