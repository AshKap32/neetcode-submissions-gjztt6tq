class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        # If its already a palindrome we dont have to check
        if s == s[::-1]:
            return True

        copy = s[:]

        for i, char in enumerate(s):
            
            # Skip past alpha numeric
            if not char.isalnum():
                continue
            
            copy.pop(i)
            print(f"removed: {char}, copy: {copy}, copy_r: {copy[::-1]}")
            # Check if reversed is equivlent
            if copy == copy[::-1]:
                return True

            # Reset copy
            copy = s[:]

        return False