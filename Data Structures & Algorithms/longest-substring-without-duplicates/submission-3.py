class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        l = 0
        # have a set to track the characters we've seen
        seen = set()
        for r, char in enumerate(s):
            
            # while we are out of equilibrium (IE the next character we're adding in is a duplicate)
            # lets remove the character from the seen set on the left most side (left side is the
            # Last valid window side) until the duplicate is out
            while char in seen:
                seen.remove(s[l])
                l += 1

            # we then add to the seen set and track the longest window size since we're back in equilibrium
            seen.add(char)
            longest = max(longest, r - l + 1)
        return longest
           
            
