class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        


        prefix = []
        total = 1
        zero_count = 0

        # If value is 0 increment zero amount, else just add it to a
        # Prefix Product Array which takes the running total.
        # By Avoiding the Zero we are able ot get the total value it was supposed
        # to be before mulitplying by the zero.
        for num in nums:
            if num == 0:
                zero_count += 1
                continue
            total *= num
            prefix.append(total)
        
        # If the zero count is above 1, then the entire array would end up being
        # 0, this is because even if you wanted to take all but self, if another val
        # is 0, then youd get all Zeros
        if zero_count > 1:
            return [0] * len(nums)
        
        # Going to have upto len(nums) values in array
        res = [0] * len(nums)
        for i in range(len(nums)):
            # If count and nums[i] is 0 then append the total product (since we skipped mulitplying by 0 in prev for loop).
            if zero_count and nums[i] == 0:
                res[i] = prefix[-1]
                return res
            if not zero_count:
                # Value is the total product (last value) divided by current num
                val = prefix[-1] // nums[i]
                res[i] = val
        return res        