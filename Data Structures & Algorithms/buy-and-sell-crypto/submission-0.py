class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        right = len(prices) - 1
        for left, price in enumerate(prices):
            while left < right:
                maxProfit = max(maxProfit, prices[right]-price)
                right -= 1
            right = len(prices) - 1
        return maxProfit
