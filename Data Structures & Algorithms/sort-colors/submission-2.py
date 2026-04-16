class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Bucket Sort so O(3n), making the number accessibile by its index. This will allow us to put values in the array at o(1) because its accessed by index directly.
        colors = [0] * (max(nums) + 1)

        # Increment the freq of that number inside of colors
        for num in nums:
            # O(1) accessing then incrementing the freq
            colors[num] += 1

        i = 0
        # Going by len because we know each index is a num in the orginal array
        for num in range(len(colors)):
            # Max is O(n) since we are iterating over the entire array once
            for _ in range(colors[num]):
                nums[i] = num
                i += 1
        
