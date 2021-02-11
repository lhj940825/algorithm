'''
 * User: Hojun Lim
 * Date: 2021-02-07
'''

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freqs = nums[::2]
        vals = nums[1::2]

        freq_val_pairs = zip(freqs, vals)
        decompressed_nums = []
        for freq, val in freq_val_pairs:
            decompressed_nums.extend([val for _ in range(freq)])

        return decompressed_nums

        