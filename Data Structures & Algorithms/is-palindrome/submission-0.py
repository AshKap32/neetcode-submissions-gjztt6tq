class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Can have two pointers, one starting at the end, one
        # Starting at 0. Once the left is >= rihgt or while l < r
        # Compare values, if same we continue, else false 
        # Break out of loop return True.

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                print(s[l], s[r])
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            elif not s[l].isalnum():
                l += 1
            else:
                r -= 1
        return True