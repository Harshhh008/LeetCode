class Solution:
    def makeFancyString(self, s: str) -> str:
        hash_map = {}
        result = []
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1

            if hash_map[s[i]] < 3:
                result.append(s[i])
                
        return ''.join(result)