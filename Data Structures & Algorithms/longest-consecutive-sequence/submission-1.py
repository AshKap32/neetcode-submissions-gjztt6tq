class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numS = set(nums)
        res = 0

        for num in numS:
            if num - 1 not in numS:
                seq = 1
                while num+seq in numS:
                    seq += 1
                res = max(res, seq)

        return res