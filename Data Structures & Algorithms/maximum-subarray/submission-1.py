class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array = -1
        running_total = 0
        for i, num in enumerate(nums):
            running_total += num
            max_sub_array = max(max_sub_array, running_total)
            if running_total < 0:
                running_total = 0
            
        return max_sub_array