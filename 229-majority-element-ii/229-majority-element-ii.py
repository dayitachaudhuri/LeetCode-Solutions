class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        elem1 = elem2 =None 
        freq1 = freq2 = 0 
        for val in nums:
            if val == elem1:
                freq1 += 1
            elif val == elem2:
                freq2 += 1
            elif freq1 == 0:
                elem1 = val
                freq1 = 1
            elif freq2 == 0:
                elem2 = val 
                freq2 = 1
            else:
                freq1 -= 1
                freq2 -= 1
                
        count1 = count2 = 0
        for val in nums:
            if val == elem1:
                count1 += 1
            elif val == elem2:
                count2 += 1
        
        ans = []
        if count1 > len(nums) // 3:
            ans.append(elem1)
        if count2 > len(nums) // 3:
            ans.append(elem2)
            
        return ans
            