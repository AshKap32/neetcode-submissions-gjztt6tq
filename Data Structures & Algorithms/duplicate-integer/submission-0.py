class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        countMap = {}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
                return True
            else:
                countMap[num] = 1
        return False
        