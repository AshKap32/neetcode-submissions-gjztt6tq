class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of array prefix sum = last value is the total product, so to 
        # Get the product without the value you are on, all you do is take the total / it
        # by the number you are on, and that is the product of every other item except the oen 
        # You are on.

        prefixSum = []
        zero_count = 0
        product = 1
        # Can use the prefix sum to solve this problem have to track the 0s
        for num in nums:
            if num != 0:
                product *= num
                prefixSum.append(product)
            else:
                   # If we hit a 0 thenw e keep track of that But continue filling in the rest of them. 
                zero_count += 1

        # If we have more than one zero then the entire array would be full 
        # with zeros
        output = [0] * len(nums)

        if zero_count > 1:
            return output

        # Else we iterate over nums again and we use the prefixSum array
        # and we can dividie it by itself.
        for i, num in enumerate(nums):
            if zero_count == 1 and num == 0:
                output[i] = prefixSum[-1]
                return output
            # This case only executes if there were no zeros in nums so both
            # Prefix Sum array and nums are the same length
            elif zero_count == 0:
                output[i] = prefixSum[-1] // num

        return output
        # quick walk through: prefixSum = [1, 2, 8, 48] output = [48, 24, 12, 8]
        # quick second edge case walkthrough: zero_count = 1, prefixSum = [-1, -1, -2, -6] output = [0, -6, 0, 0, 0]



        #if we have one zero then we go ahead and fill 0's for everything else
        # and once we hit the num thats 0 we fill in the last prefixSum value

