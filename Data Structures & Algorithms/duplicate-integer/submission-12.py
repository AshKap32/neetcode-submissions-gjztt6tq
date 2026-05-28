class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # We can track via a set to see which values we have seen
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False