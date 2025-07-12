class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_arr = [0] * int(len(nums) +  1)
        for num in nums:
            new_arr[num] += 1
        
        not_appear = []
        for i in range(1, len(new_arr)):
            if new_arr[i] == 0:
                not_appear.append(i)
        
        return not_appear