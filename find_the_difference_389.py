class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in set(t):
            if s.count(ch) != t.count(ch):
                return ch
        return ""

        #using hash map
        # hash_map= {}
        # unique = []

        # for st in s:
        #     if st in hash_map:
        #         hash_map[st] += 1
        #     else:
        #         hash_map[st] = 1
        # for st in t:
        #     if hash_map.get(st, 0) <= 0:
        #         unique.append(st)
        #     else:
        #         hash_map[st] -= 1

        # return "".join(unique)