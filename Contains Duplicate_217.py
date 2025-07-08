#first method

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seem = set()
        for i in nums:
            if i in seem:
                return True
            seem.add(i)
        return False
    


#second method

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    