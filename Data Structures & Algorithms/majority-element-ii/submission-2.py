class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        major = n // 3
        count_of = 0

        i = 1 
        curr = 1
        if n <= 2:
            return nums
        print(nums)
        while i <= n - 1:
           # Increment the curr count to the right value 
            if nums[i] == nums[i-1]:
                curr += 1

            # Not the same OR at the end of the list 
            if nums[i] != nums[i-1] or i == n - 1:
                print(nums[i], nums[i-1], i, n-1, f"major: {major}, curr: {curr}")
                if curr > major:
                    nums[count_of] = nums[i-1]
                    count_of += 1
                # Current should still be reset either way back to one so it doesnt accidentally track another value
                curr = 1
            i += 1

        return nums[:count_of]