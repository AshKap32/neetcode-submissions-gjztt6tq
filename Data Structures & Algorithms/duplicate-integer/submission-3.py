class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = {}
        for i, num in enumerate(nums):
            if num not in countMap:
                countMap[num] = i
            else:
                return True
        return False
