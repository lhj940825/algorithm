'''
 * User: Hojun Lim
 * Date: 2020-12-16
'''

class Solution:
    def sortString(self, s: str) -> str:
        import copy
        dic = {}
        for i, char in enumerate(s):
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        dic = dict(sorted(dic.items(),key= lambda x: x[0]))


        output = ''
        while dic: # if dic is empty, stop
            keys = deepcopy(dic).keys()
            for key in keys:
                output += key
                dic[key] -= 1

                if dic[key] == 0:
                    dic.pop(key)

            keys = list(dic.keys())

            reverse_keys = keys[::-1]
            for key in reverse_keys:
                output += key
                dic[key] -= 1

                if dic[key] == 0:
                    dic.pop(key)

        return output