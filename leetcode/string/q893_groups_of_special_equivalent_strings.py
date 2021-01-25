'''
 * User: Hojun Lim
 * Date: 2021-01-25
'''

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        decomposed_A = {} # store the set of unique char in odd and even indicies, respectively
        for a in A:
            key = (tuple(sorted(a[::2])), tuple(sorted(a[1::2])))

            if key in decomposed_A:
                decomposed_A[key] += 1
            else:
                decomposed_A[key] = 1

        #special_equivalent_cnt = 0
        return len(decomposed_A)


