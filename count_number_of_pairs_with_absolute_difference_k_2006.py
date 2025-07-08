class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    if nums[i] - nums[j] == k:
                        count += 1
        return count