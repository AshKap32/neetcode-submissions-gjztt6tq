class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # A squence starts ehen the value behind it is not present, we don't care about duplciates but want O(1) search

        nums_set = set(nums)

        if not nums:
            return 0
        
        longest = 1

        # for each of the num in nums 
        for i, num in enumerate(nums):
            # Start of sequence
            if num - 1 not in nums_set:
                # if we get here reset that means its at least one
                current = 1

                # while num + current (sequence ahead of num) is in the set continue (O(1) lookup)
                while num + current in nums_set:
                    current += 1
                
                # Save once broken out
                longest = max(longest, current)
        
        return longest

                
