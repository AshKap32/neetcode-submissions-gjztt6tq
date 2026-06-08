class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 0;
        int profit = 0;

        while (r < prices.length) {

            while (l < r && prices[l] > prices[r]) {
                l++;
            }

            profit = Math.max(profit, prices[r] - prices[l]);
            r++;
        }

        return profit;

    }
}
