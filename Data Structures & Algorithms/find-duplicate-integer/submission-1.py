class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        # O(n) time and space complexity
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return nums[i]
        #     seen.add(nums[i])
        
        # Can also sort it for O(1) space 
        sorted_n = sorted(nums)

        l, r = 0, 1
        
        while r <= len(nums) - 1:
            if sorted_n[l] == sorted_n[r]:
                return sorted_n[r]
            l += 1
            r += 1
            
