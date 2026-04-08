class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        # O(n) time and space complexity
        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return nums[i]
        #     seen.add(nums[i])
        
        # Can also sort it for O(1) space   
        

        l, r = 0, 1
        nums.sort()
        while r <= len(nums) - 1:
            if nums[l] == nums[r]:
                return nums[r]
            l += 1
            r += 1

