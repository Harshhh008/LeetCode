class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time limit exceeded
        # new_lst = []
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
        #                 if not sorted([nums[i], nums[j], nums[k]]) in new_lst:
        #                     new_lst.append(sorted([nums[i], nums[j], nums[k]]))
        # return new_lst


        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result