class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n = len(nums)
        majority = n / 2

        for i, num in enumerate(nums):
            freq[num] += 1
        
        for num, freq in freq.items():
            if freq > majority:
                return num
            