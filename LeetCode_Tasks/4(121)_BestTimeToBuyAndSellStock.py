"""
You are given an array prices_input where prices_input[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution(object):
    def maxProfit(self, prices_input):
        """This solution takes a lot of time for searching result O(n^2)"""
        max_profit = 0
        for first_day_index, first_day_price in enumerate(prices_input):
            for second_day_index, second_day_price in enumerate(prices_input[first_day_index + 1:]):
                if second_day_price - first_day_price > max_profit:
                    max_profit = second_day_price - first_day_price
        return max_profit

    def maxProfit2(self, prices_input):
        """The best solution with spending time O(n)"""
        profit = 0
        min_price = prices_input[0]
        for price in prices_input:
            if price < min_price:
                min_price = price
            profit = (price - min_price) if (price -
                                             min_price > profit) else profit
        return profit


prices = [7, 5, 3, 6, 4, 1]
sol = Solution()
print(sol.maxProfit(prices))
