class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Assumign that every value has exactly one par, we can 
        # Create a solution that is worst case O(n) by using a 
        # Hashmap, and check to see if the comp exists in the map

        f_map = {}

        for idx, num in enumerate(nums):
            # See's if the value we need exists in the mpa
            comp = target - num
            # O(1) look up
            if comp in f_map:
                # Returns teh indexes of that value
                return [f_map[comp], idx]
            f_map[num] = idx
        return []