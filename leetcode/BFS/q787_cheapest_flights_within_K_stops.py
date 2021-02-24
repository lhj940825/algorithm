'''
 * Project : algorithm
 * Package : 
 * User    : jun
 * Date    : 2021/02/24
 * Time    : 8:15 오후
'''

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from collections import defaultdict, deque
        import sys

        src2dst = defaultdict(list)
        for flight in flights:
            src2dst[flight[0]].append({'dst': flight[1], 'price':flight[2]})


        que = deque()
        que.append((src, 0))
        k = 0
        prices = [sys.maxsize]

        while que and k <= K:
            for _ in range(len(que)):
                cur_stop = que.popleft()
                _dst_list = src2dst[cur_stop[0]]

                for _dst in _dst_list:
                    if dst == _dst['dst']:
                        prices.append( cur_stop[1] + _dst['price'])

                    else:
                        # in order to remove the unlikely candidate to prevent the time limit
                        cum_price = cur_stop[1] + _dst['price'] # sum of the price to reach the current stop and to get the _dst
                        if cum_price < min(prices):
                            que.append((_dst['dst'], cum_price))

            k += 1

        prices = prices[1:]
        return -1 if len(prices) == 0 else min(prices)

