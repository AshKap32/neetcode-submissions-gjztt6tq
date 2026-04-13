class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Assumign that every value has exactly one par, we can 
        # Create a solution that is worst case O(n) by using a 
        # Hashmap, and check to see if the comp exists in the map

        freq = {}

        for i, num in enumerate(nums):
            comp = target - num

            if comp in freq:
                return [freq[comp], i]
            
            freq[num] = i
        return []