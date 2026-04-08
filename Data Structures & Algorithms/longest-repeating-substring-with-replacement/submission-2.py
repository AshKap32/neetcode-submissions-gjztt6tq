class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

              
        count = defaultdict(int)
        longest = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            # Increments count in the window
            count[s[r]] += 1
            # Sets the max_freq character in the window
            max_freq = max(max_freq, count[s[r]])

            # If window is invalid = window len - max_freq > k
            # Window works as long as the max freq character - window len is <= k 
            # Since we can replace the other characters with the replacement
            while (r-l+1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest
