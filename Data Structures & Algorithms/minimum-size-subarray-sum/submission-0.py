class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_len, l, total = 100000, 0, 0

        for r, num in enumerate(nums):
            total += num
            while total >= target:
                min_len = min(min_len, r - l + 1)
                total -= nums[l]
                l += 1
            

        if min_len == 100000:
            return 0
        
        return min_len