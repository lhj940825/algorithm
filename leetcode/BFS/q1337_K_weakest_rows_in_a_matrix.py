'''
 * User: Hojun Lim
 * Date: 2021-01-12
'''

# q1337 The K Weakest Rows in a Matrix
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_power_pairs = []
        for i in range(len(mat)):
            row_power_pairs.append( (i, bnSearch(mat[i], 0, len(mat[i])-1, len(mat[i]))))

        row_power_pairs.sort(key=lambda x:x[1])
        return [pair[0] for i, pair in enumerate(row_power_pairs) if i < k]



def bnSearch(row, start, end, idx):
    if start > end:
        return idx

    mid = (start+end)//2
    val = row[mid]

    if val == 1:
        start = mid + 1
        idx = bnSearch(row, start, end, idx)

    elif val == 0:
        idx = mid
        end = mid - 1
        idx = bnSearch(row, start, end, idx)

    return idx