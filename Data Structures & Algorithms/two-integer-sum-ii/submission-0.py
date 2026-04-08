class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two methods here that we can use, since a hash map is in play we could iterate
        # Through the entire list until we find the diff in the hashmap, else we add int the num

        # Or now since it is sorted, we know that if the value is greater than the target 
        # Can decrease it from the left else, if its less than the target we increase it from the left
        # if its = to the target reutrn index l,r + 1
        # Do till we get to the middle of the list

        l,r = 0, len(numbers) - 1
        while l < r:
            val = numbers[l] + numbers[r]
            if val == target:
                return [l + 1, r + 1]
            elif val > target:
                r -= 1
            else:
                l += 1
        