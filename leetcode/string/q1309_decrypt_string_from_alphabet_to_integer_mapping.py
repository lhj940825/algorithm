'''
 * User: Hojun Lim
 * Date: 2021-01-30
'''

import re

class Solution:
    def freqAlphabets(self, s: str) -> str:
        a = [m.start() for m in re.finditer('#',s)]


        output = ''
        i = 0
        while i < len(s):
            if i+2 in a:
                output += chr(int(s[i:i+2])+96)
                i += 3

            else:
                output += chr(int(s[i])+96)
                i += 1


        return output
