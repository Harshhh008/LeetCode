class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k = 2

        # for i in range(2, len(nums)):
        #     if nums[i] != nums[k - 2]:
        #         nums[k] = nums[i]
        #         k += 1
        # return k

        # using hash_map
        hash_map = {}
        k = 0
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
            if hash_map[nums[i]] <= 2:
                nums[k] = nums[i]
                k += 1
        return k
        