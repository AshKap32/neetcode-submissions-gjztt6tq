class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Trying to return the length, and the sequence is one in which there 
        # Exists a value 1 above the previous one.
        # What we can do is convert nums to a set to provide o(1) lookup
        # and What we can do is loop thru the set and check to see if the current num + 1 exists in the set
        # if it does we add 1 to the seqence. Else we continue to the next value and since 
        # we are using the o(1) lookup to have an inner while loop the time cmplexity is O(n)

        nums_set = set(nums)
        max_length = 0

        if len(nums_set) == 1:
            return 1
        #O(n) since iterating thru entire set
        for num in nums_set:
            if (num + 1) in nums_set:

                # This means we encountered a sequence of AT LEAST one
                length = 1
                # Curr num is now set to be the value we are at
                curr_num = num

                # O(1) lookup so looping in O(1) time
                while curr_num + 1 in nums_set: 
                    length += 1
                    curr_num += 1
                # Set max len
                max_length = max(max_length, length)
        return max_length
            
