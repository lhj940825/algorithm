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

################################################################################
# solution with out sorting
################################################################################

class Solution(object):
    def numSpecialEquivGroups(self, A):
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            print(ans)
            return tuple(ans)

        return len({count(word) for word in A})
