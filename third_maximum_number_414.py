class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # first = second = third = float("-inf")
        # for num in nums:
        #     if num in (first, second, third):
        #         continue
        #     if num > first:
        #         first, second, third = num, first, second
        #     elif num > second:
        #         second, third = num, second
        #     elif num > third:
        #         third = num

        # return third if third != float("-inf") else first


        #0ms
        nums = list(set(nums))
        if len(nums) <= 2:
            return max(nums)
        else:
            nums.sort(reverse=True)
            return nums[2]
        
