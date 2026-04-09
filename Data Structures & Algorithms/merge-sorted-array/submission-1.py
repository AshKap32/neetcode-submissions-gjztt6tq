class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start by inserting one of the values at the very end n-m position of the array (in the back) then decrement n by 1
        ## After that start comparing that value to the value below it so right and left pointers 
        ## Compare the two and swap if the left value is greater than the right 
        # Else they are in the right position so we stop 

        for num in nums2:
            # places in the next 0th position
            nums1[-n] = num
            
            # i is a 
            i = m

            # bubble down
            while i > 0:
                # that means value below is greater so we swap
                if nums1[i-1] > nums1[i]:
                    nums1[i-1], nums1[i] = nums1[i], nums1[i-1]
                    # decrement i to check the next value,. if needed will go all the way to the 0th position
                    i -= 1
                else:
                    # this means we are at the correct position we can break
                    break


            # increment m for the next inserted position in nums1, decrement n for the next 0th position in nums1
            m += 1
            n -= 1


