class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = []
        
        for i in range(len(nums)):
            if nums[i] == target:
                if len(index) == 2 and i > index[-1]:
                    index[-1] = i
                else:
                    index.append(i)

        if len(index) == 1:
            return index*2
        elif len(index) < 1:
            return [-1, -1]
        else:
            return index