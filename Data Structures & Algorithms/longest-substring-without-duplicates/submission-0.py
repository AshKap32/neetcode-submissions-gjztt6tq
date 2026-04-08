class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_sub = 0
        seen = set()
        left = 0

        for right, ch in enumerate(s):
            while ch in seen:
                left_ch = s[left]
                seen.remove(left_ch)
                left += 1
            
            seen.add(ch)
            longest_sub = max(longest_sub, right - left + 1)
        return longest_sub
