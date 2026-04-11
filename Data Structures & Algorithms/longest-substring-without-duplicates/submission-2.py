class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        """

        This works because we ensure we are always in a valid window state, so if we iterate 
        over the enitre string without having dupes, we always record teh max window len

        """

        # Need something to keep track of the max sub string
        # Can use a two pointer system
        # Have to know which values are in the current window, but want O(1) lookup so can use a set
        l = 0
        seen = set()
        longest = 0

        # One pointer is the start of the valid window, the next iterates over the string
        for r in range(len(s)):
       
            # Before we add in a value we check if it is in seen set
            while s[r] in seen:
                # If its in that set we take the left most value (start of valid window) and remove it from the set
                # We then increment l by one, continue until we get rid of the duplicate
                seen.remove(s[l])
                l += 1
            
            # Add the char to the seen set after we are back to equilibrium
            # Record the max window length
            seen.add(s[r])
            longest = max(longest, r - l + 1)

        return longest


           
            
