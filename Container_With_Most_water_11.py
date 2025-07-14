class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_value = 0
        left = 0
        right = len(height) - 1

        while left < right:
            min_value = min(height[left], height[right]) * (right - left)
            max_value = max(min_value, max_value)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_value