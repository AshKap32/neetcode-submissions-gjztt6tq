class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # Quick way
        # return nums + nums

        # other way
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        
        for i in range(len(nums)):
            ans.append(nums[i])
        return ans
        