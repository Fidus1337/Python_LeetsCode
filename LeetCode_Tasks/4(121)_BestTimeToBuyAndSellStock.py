"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for first_day_index, first_day_price in enumerate(prices):
            for second_day_index, second_day_price in enumerate(prices[first_day_index + 1:]):
                if second_day_index <= first_day_index:
                    continue
                elif second_day_price - first_day_price > max_profit:
                    max_profit = second_day_price - first_day_price
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.maxProfit(prices))
