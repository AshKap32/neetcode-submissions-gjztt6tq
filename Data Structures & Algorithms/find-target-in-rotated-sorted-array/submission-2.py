class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Need to check in which portion the target exists, IE does it exist in the sorted portion
        # which can be determined by check do an inital check before this to see if nums[m] = target: return m then check
        # if nums[m] >= nums[l]: if nums[l] <= target < nums[m]: r = m - 1
        #if nums[m] < nums[l] (then we are in the unsorted portion) and if nums[l] > target


        # Actually we should check to see if the value is first contained between l and m and if it is, we can cut the array in half

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            print(nums[l], nums[m], nums[r])
            if nums[m] == target:
                return m 
            
            # if the order is correct:
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: 
                print("broke in")
                # that means left value was likely wrapped around so if the left value is greater than the target
                # then the value liekly lies in the other portion
                # Else if the nums[l] <= target then the value liekly lies in the left portion so r = m -1
                if nums[l] > target:
                    # Checks to see if target is greater then l = m + 1 else r = m - 1 since the 
                    # target lies in between l and m
                    if nums[m] < target:
                        l = m + 1
                    else:
                        r = m - 1

                else:
                    r = m - 1
            

            
        return -1