class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hash_map = Counter(nums1)
        result = []
        hash_map = {}
        for num in nums1:
            if num in hash_map.keys():
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        for num in nums2:
            if hash_map.get(num, 0) > 0:  # if i don't use counter so use get method it don't give key error when i use get 
                result.append(num)
                hash_map[num] -= 1
        return result