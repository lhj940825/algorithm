'''
 * User: Hojun Lim
 * Date: 2020-12-16
'''
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hash_map = []
        for i in range(len(s)):
            hash_map.append((s[i], indices[i]))

        hash_map = sorted(hash_map, key=lambda x:x[1])

        output = ''
        for i in range(len(hash_map)):
            output+= hash_map[i][0]

        # above for loop can be substitute by
        output = ''.join(hash_map[i][0] for i in range(len(hash_map)))
        return output
