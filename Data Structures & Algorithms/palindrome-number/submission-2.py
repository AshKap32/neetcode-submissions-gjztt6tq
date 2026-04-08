class Solution:
    def isPalindrome(self, x: int) -> bool:
      
        str_x = str(x)
        l, r = 0, len(str_x) - 1



        # Iterate from the left and right until you meet in the middle IE while l <= r
        while l < r:
            if str_x[l] == str_x[r]:
                l += 1
                r -= 1
                continue 
            else:
                return False
           
        return True


            