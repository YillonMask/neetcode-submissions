class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = prices[0]
        max_profit = -1
        for i in range(len(prices)):
            cur_price = prices[i]
            if cur_price < start:
                start = cur_price
            profit = cur_price - start
            if profit > max_profit:
                max_profit = profit
        
        return max_profit