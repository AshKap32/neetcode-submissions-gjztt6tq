class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # So we are trying to see if the value appears more than once
        # So we need a method in order to track which value we have just seen
        # The quickest way to do that and provide O(1) lookup would be by using a set
        # However having a set would make iur spac complexity O(n). But it would make 
        # the worstcase time complexity O(n)
    
        # track the ones we have seen
        seen = set()

        for num in nums:
            # dup found o(1) lookup in sets and hashmaps
            if num in seen:
                return True
            seen.add(num)
        
        return False
