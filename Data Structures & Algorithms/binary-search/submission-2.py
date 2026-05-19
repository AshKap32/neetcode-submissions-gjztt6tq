class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Because it is alreay sorted, we can use binary searching
        # have. aleft and right pointer, one starting at the beginning 
        # and one starting at the end of the array
        # we then go until l < r
        # caluclate the mid pointer = (r - 1) // 2
        # check to see if nums[mid] > target if so r = mid - 1
        # check to see if nums[mid] < target if so l = mid + 1
        # check to see if nums[mid] == target then return mid
        # if we break out return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1