class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r, profit = 0, 0, 0

        while r < len(prices):

            while l < r and prices[l] > prices[r]:
                l += 1

            profit = max(profit, prices[r] - prices[l])
            r += 1

        return profit 