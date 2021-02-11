'''
 * User: Hojun Lim
 * Date: 2021-02-07
'''

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        min_side_lengths = list(map(lambda x: min(x), rectangles))

        from collections import defaultdict
        length_cnt = defaultdict(int)
        for side_length in min_side_lengths:
            length_cnt[side_length] += 1

        return length_cnt[max(length_cnt.keys())]