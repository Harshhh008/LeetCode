# 136
def singleNumber(self, nums):
    ans = 0
    for x in nums:
        ans ^= x
    return ans

#1.
def twoSum(self, nums, target):
    n = len(nums)
    start = 0
    next = 1
    for i in range(start, n-1):
        for j in range(next, n):
            if not i == j and nums[i] + nums[j] == target:
                return [i,j]

#53. max sub array
def maxSubArray(self, nums):
    current_sum = 0
    max_sum = float("-inf")
    for i in range(len(nums)):
        current_sum += nums[i]
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
    return max_sum
        