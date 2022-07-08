class Solution:
    def trap(self, height: List[int]) -> int:
        area = 0
        left_bar, right_bar = 0, len(height) - 1

        while left_bar < right_bar - 1:
            if height[left_bar] <= height[left_bar + 1]:
                left_bar += 1
            elif height[right_bar] <= height[right_bar - 1]:
                right_bar -= 1
            else:
                if height[left_bar] > height[right_bar]:
                    curr = right_bar - 1
                    while height[curr] < height[right_bar]:
                        area += (height[right_bar] - height[curr])
                        curr -= 1
                    right_bar = curr
                else:
                    curr = left_bar + 1
                    while height[curr] < height[left_bar]:
                        area += (height[left_bar] - height[curr])
                        curr += 1
                    left_bar = curr

        return area