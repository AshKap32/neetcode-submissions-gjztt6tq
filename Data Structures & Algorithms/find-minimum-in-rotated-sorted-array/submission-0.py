class Solution:
    def findMin(self, nums: List[int]) -> int:
        # What we can do is have res set to the first value (in case its the smallest)
        res = nums[0]
        l, r = 0, len(nums) - 1

        # While l <= r becuase worst case we meet at the mid point where l == r

        while l <= r:
             # If the right value is greater than the left then we are at the smallest value
             # Not the case if the array is rotated
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
    
            # Getting the middle value, updating the res to the smallest between mid and the current
            # res becuase if we are on the smallest value right now then we have to update it assuming this is the start of the 
            # Asscessnding portion
            m = (l+r) // 2
            res = min(res, nums[m])

            # if right value (mid is) greater than the left value this portion is properly sorted
            # so the right portion must be the smaller portion else the left value is greater then the mid 
            # if thats the case that means 
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

