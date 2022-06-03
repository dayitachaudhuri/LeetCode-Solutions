class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        elem1 = elem2 = 0
        c1 = c2 = 0 
        
        for val in nums:
        
            if val == elem1:
                c1 += 1
            elif val == elem2:
                c2 += 1
            elif c1 == 0:
                elem1 = val
                c1=1
            elif c2 == 0:
                elem2 = val 
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
                
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
            