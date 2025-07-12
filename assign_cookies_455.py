class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        enough_cookie = 0

        g.sort()
        s.sort()

        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                enough_cookie += 1
                i += 1
            j += 1
        
        return enough_cookie

