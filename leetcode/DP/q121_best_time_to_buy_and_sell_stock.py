'''
 * User: Hojun Lim
 * Date: 2021-01-18
'''

import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = [None]*len(prices)
        buy_price = prices[0]
        max_profit[0] = -sys.maxsize -1
        prices = prices[1:]
        for i, price in enumerate(prices, start = 1):

            if max_profit[i-1] < price - buy_price:
                max_profit[i] = price - buy_price
            else:
                max_profit[i] = max_profit[i-1]

            if price < buy_price:
                buy_price = price


        _max_profit = -1
        for profit in max_profit:
            if profit > _max_profit:
                _max_profit = profit

        if _max_profit < 0 :
            return 0
        else:
            return _max_profit

        return max(max_profit)

