class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # freq = defaultdict(int)
        n = len(nums)
        majority = n / 2

        # for i, num in enumerate(nums):
        #     freq[num] += 1
        
        # for num, freq in freq.items():
        #     if freq > majority:
        #         return num
        nums.sort()
        maxCount = 0
        maxNum = -1
        currentCount = 1
        # [1, 1, 1, 5, 5, 5, 5]
        if n <= 1:
            return nums[0]
        for i in range(1, n):
            maxCount = max(maxCount, currentCount)
            if maxCount == currentCount:
                maxNum = nums[i-1]

            if nums[i] == nums[i - 1]:
                currentCount += 1
                print(currentCount)
            else:
                currentCount = 1

            
         
        return maxNum