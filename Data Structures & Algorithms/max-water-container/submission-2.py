class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Max Area = [r-l] * heights[i]
        # Have a running total of the heights        
        # Two pointers, one starting on the end, one in the beginning 
        max_area = 0
        l, r = 0, len(heights) - 1


        # Once we get to l < r break the while loop 
        while l < r:

        # Only move the index that has a smaller height, in a way sliding window
        # Does not hurt to check allk the values, but theoretically can make it faster if 
        # We check to see if the one we are moving to is greater than the previous val
        # If it isn't we can skip the curr and move onto the next.

            # Calc the area, set max_area
            area = (r - l) * min(heights[r], heights[l])
            print(max_area, area)
            max_area = max(max_area, area)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        print(max_area)
        return max_area

        

