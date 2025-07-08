class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for wd in patterns:
            if wd in word:
                count += 1
        return count