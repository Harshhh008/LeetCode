class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # using hash map
        s_map = {}
        t_map = {}

        for s_str in s:
            if s_str in s_map:
                s_map[s_str] += 1
            else:
                s_map[s_str] = 1
        
        for t_str in t:
            if t_str in t_map:
                t_map[t_str] += 1
            else:
                t_map[t_str] = 1
        return s_map == t_map