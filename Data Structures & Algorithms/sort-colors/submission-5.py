class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
         # three pointers
        l, m, h = 0, 0, len(nums) - 1

        # Mid is traversing the array, low is where the next 0 can go, h is where the next 2
        # goes
        while m <= h:
            # if we find a 0, swap with low becuase low is at 1 (the next availble spot for a 0)
            # We can increment mid and l to continue searching since we skip over 1s and we know
            # that mids, location now has a 1. this is becuase 1s are going to be in the
            # middle, and we know all values from low - mid are going to be ones, 
            # and 0-low-1 are going to be 0s only one we want to re check is when 
            # we swap from the end to mid  since that is unexplored
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 1:
                m += 1
            elif nums[m] == 2:
                nums[m], nums[h] = nums[h], nums[m]
                h -= 1
            
