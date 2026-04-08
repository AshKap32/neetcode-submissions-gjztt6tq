class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = []
        for i in range(max(nums) + 1):
            colors.append(0)

        for n in nums:
            colors[n] += 1
        
        i = 0
        for n in range(len(colors)):
            for _ in range(colors[n]):
                nums[i] = n
                i += 1


        