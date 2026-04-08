class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """

        Sound like we need a window in s2 that checks to see if it matches s1 
        One of the conditions would be to ensure the window is the same length 
        as S1. If either of these conditons are broken then
        we increment our left pointer until we are back in equilibrium.

        Then we check to see if the freq in s1 and s2 are the same, if they are then we
        return true, else we continue the while loop until we are at the end of len(s2).
        
        Worst case time complexity in ths case is O(n) since we iterate just over one.
        
        So we can have a freq map of s1 and then while we iterate over, we can add that
        value to its own freq map, if the conditon (r-l+1) > len(s1)) then we would 
        take if freq_map[s[l]] == 1 then we freq_map.pop(s[l]) else freq_map[s[l]] -= 1.

        if we get out of the loop we return False.

        """

        l = 0
        f_map = defaultdict(int)

        # Getting Freq of s1
        for idx, char in enumerate(s1):
            f_map[char] += 1
        
        # Map to track s2 values
        t_map = defaultdict(int)

        for r in range(len(s2)):
            
            t_map[s2[r]] += 1

            while (r - l + 1) > len(s1):
                if t_map[s2[l]] == 1:
                    t_map.pop(s2[l])
                else:
                    t_map[s2[l]] -= 1
                l += 1
            
            if t_map == f_map:
                return True

        return False

            
