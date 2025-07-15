class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len