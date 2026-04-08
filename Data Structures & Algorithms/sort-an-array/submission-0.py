class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        s_arr = []

        for i, num in enumerate(nums):

            # Insert value into new array to sort it and j is the index of the value we jsut added
            s_arr.append(num)
            j = len(s_arr) - 1

            # Should just be up to o(n) anyways since we only go down n elements that we are already iterating over
            # if the value ever hits 0 we want to break out of the while loop.
            while j > 0:
                # If the current value is greater than or equal to the value before it 
                # since its already sorted, we can break out of this part of the loop
                if s_arr[j] >= s_arr[j-1]:
                    break
                
                # if its less than the value before we swap things around
                elif s_arr[j] < s_arr[j-1]:
                    temp = s_arr[j]
                    s_arr[j] = s_arr[j-1]
                    s_arr[j-1] = temp
                
                # Decrement j
                j -= 1
            
        return s_arr
