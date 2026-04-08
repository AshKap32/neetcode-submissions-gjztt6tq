class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums.sort()
        # Two pointers:

        # Figure out the value l - r see if an index of it exists, if it doesn't


        # Sorts nums, 0 is in the middle, we only want to iterate till 0, since that will check all the values
        # if tis the same value as before, we can skip since it is reduandent 
        # left pointer is one index above i, right is end of the array
        # till youve met in the middle, use the number you're curently on an iterate 
        # over the array, if total > 0 then the right is too big, so decrease
        # if total < 0 left is too negative so icnrease by 1, else its equal to 0 
        # so add the values in an array, and increment left whiel decremting right
        # while the left value is equal to the next value increment l
        ## Has a left and right
        res = []
        for i, num in enumerate(nums):
            #Break if over 0 since we have gone over all possibilities already
            if num > 0:
                break
            
            # Avoid duplicate numbers
            if i > 0 and num == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l +=1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
