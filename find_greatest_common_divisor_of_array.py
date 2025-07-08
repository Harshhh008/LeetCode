class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest_num = min(nums)
        largest_num = max(nums)

        return gcd(smallest_num, largest_num)