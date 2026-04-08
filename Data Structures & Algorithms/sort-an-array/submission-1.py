class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Insertion Sort
        # s_arr = []

        # for i, num in enumerate(nums):

        #     # Insert value into new array to sort it and j is the index of the value we jsut added
        #     s_arr.append(num)
        #     j = len(s_arr) - 1

        #     # Should just be up to o(n) anyways since we only go down n elements that we are already iterating over
        #     # if the value ever hits 0 we want to break out of the while loop.
        #     while j > 0:
        #         # If the current value is greater than or equal to the value before it 
        #         # since its already sorted, we can break out of this part of the loop
        #         if s_arr[j] >= s_arr[j-1]:
        #             break
                
        #         # if its less than the value before we swap things around
        #         elif s_arr[j] < s_arr[j-1]:
        #             temp = s_arr[j]
        #             s_arr[j] = s_arr[j-1]
        #             s_arr[j-1] = temp
                
        #         # Decrement j
        #         j -= 1
            
        # return s_arr

        # Merge Sort 
        # Once len is less than 1 we aer at the bottom of the list and can go back up

        if len(nums) > 1:

            # Split the array down the middle
            mid = len(nums) // 2
            left_half = nums[:mid]
            right_half = nums[mid:]

            # Recurrsively call until we get to the very bottom
            
            self.sortArray(left_half)
            self.sortArray(right_half)

            i, j, k = 0, 0, 0
            while i < len(left_half) and j < len(right_half):
                # if left is smaller, it goes first, opposite if other way
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1

            # If any values remain (IE len of left half or right half is diff, copy remaining over)
            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1
            
            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1
        return nums
