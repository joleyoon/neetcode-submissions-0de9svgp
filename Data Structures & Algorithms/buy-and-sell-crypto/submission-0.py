class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = 0

        for sell in range(len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
            
            maxProfit = max(maxProfit, prices[sell] - prices[buy])

        return maxProfit