#LC 121. Best Time to Buy and Sell Stock
#CODE

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1000000000000
        profit = 0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            cost = prices[i]-min_price
            if cost > profit:
                profit = cost
        return profit
            