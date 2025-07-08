class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # 2ms
        min_value = nums[0]
        max_diff = -1

        for j in range(1, len(nums)):
            if nums[j] > min_value:
                max_diff = max(max_diff, nums[j] - min_value)
            else:
                min_value = nums[j]
        return max_diff



        # 226ms
        # max_value = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[j] - nums[i] > max_value and i < j:
        #                 max_value = nums[j] - nums[i]
        # if max_value == 0:
        #     return -1
        # return max_value
