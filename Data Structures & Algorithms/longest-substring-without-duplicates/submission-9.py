class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        l = 0
        max_sub = 0

        for r, ch in enumerate(s):
            while l < r and ch in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(ch)
            max_sub = max(max_sub, r - l + 1)
        
        return max_sub