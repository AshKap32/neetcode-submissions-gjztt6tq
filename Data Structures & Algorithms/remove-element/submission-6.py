class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # Can theoretically count the freq of val, then every time its then mvove it to the end.

        # LEft and right pointer, left pointer will scan the list for the val, rightpointer find the next good spot to swap
        # If the right pointer sees the val, then we decrement the right pointer

        # Then return len(nums) - r to be k

        r = len(nums) - 1

        for l, num in enumerate(nums):
            # if the right pointer passes the left break out of the loop
            if l > r:
                break

            # Find next valid swap value
            while nums[r] == val and r > 0:
                r -= 1

            if num != val:
                continue
            else:
                # Found val, swap them
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1

            
        return r + 1
