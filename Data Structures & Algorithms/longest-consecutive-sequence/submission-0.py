class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        streak = 0
        res = 0
        for i, num in enumerate(nums):
            
            curr = num

            if (curr - 1) not in store:
                while curr in store: #O(1)
                    streak += 1
                    curr += 1

            res = max(res, streak)
            streak = 0
        return res