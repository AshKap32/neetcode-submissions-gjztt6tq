class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area = min(heights[l], heights[r]) * (r - l)
        # Have a max area tracker initally set to 0
        # Perform the above calculation, move the left or right pointer
        # based on whats in length until you get to the end of the array
        # Two pointer as we want to move based throughout the array 
        # either way and need two values in the array at a given time.

        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:

                
            # Getting the area values
            x = r - l
            min_y = min(heights[l], heights[r])

            
            # Getting the max_area
            max_area = max(max_area, min_y * x)

            if heights[l] <= heights[r]:
                l += 1
            else: 
                r -= 1
        return max_area
            