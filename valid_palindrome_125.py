class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([x.lower() for x in s if x.isalnum()])


        if s == s[::-1]:
            return True
        else:
            return False

        #using 2 pointer approch
        # left = 0
        # right = len(s) - 1

        # while left < right:
        #     if s[left] != s[right]:
        #         return False
        #     left +=1 
        #     right -= 1
        # return True