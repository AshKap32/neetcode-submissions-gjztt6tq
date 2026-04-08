class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Track via Seen Set provides o(1) look up or can use hashmap freq
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False