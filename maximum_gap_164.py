class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
        
        max_diff = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_diff = abs(nums[i] - nums[i + 1])
                max_diff = max(curr_diff, max_diff)
        return max_diff