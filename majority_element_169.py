class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if not num in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        max_value = max(hash_map.values())
        lst = [key for key,value in hash_map.items() if value == max_value]
        return lst[0]