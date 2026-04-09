class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # have two pointers, one moving through the array and one keeping track of last not unique value
        # once we find a unique value we increment left and put the right num at that position
        # return l + 1
        l = 0
        for r in range(1, len(nums)):
            # vals are dups so continue  
            if nums[l] == nums[r]:
               continue
            # Unique so set l + 1 to the new unqiue value found, then increment to the last unqiue value
            else: 
                nums[l + 1] = nums[r]
                l += 1
        return l + 1
