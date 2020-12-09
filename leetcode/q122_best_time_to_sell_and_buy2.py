'''
 * User: Hojun Lim
 * Date: 2020-12-09
'''

import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_idx = 0
        cur_profit = 0
        while cur_idx < len(prices):
            _min_idx = self.find_min(prices, cur_idx)
            _max_idx = self.find_max(prices, _min_idx)

            if _min_idx >= _max_idx:
                break
            else:
                cur_profit += prices[_max_idx] - prices[_min_idx]

            cur_idx = _max_idx

        return cur_profit

    def find_min(self, prices, idx):
        _min =  sys.maxsize
        _min_idx = -1

        for i in range(idx, len(prices)):
            if prices[i] < _min:
                _min = prices[i]
                _min_idx = i

        return _min_idx

    def find_max(self, prices, idx):
        _max = -1*sys.maxsize+1
        _max_idx = -1

        for i in range(idx, len(prices)):
            if prices[i] > _max:
                _max = prices[i]
                _max_idx = i

        return _max_idx
