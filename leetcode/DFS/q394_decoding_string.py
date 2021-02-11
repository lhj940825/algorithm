'''
 * User: Hojun Lim
 * Date: 2021-02-11
'''

class Solution:
    def decodeString(self, s: str) -> str:
        return decode(s)


def decode(s):

    output = ''
    if '[' not in s:
        output = s
        return output

    paran_stack = []
    start_paran_idx = 0
    close_paran_idx = 0

    for idx, char in enumerate(s):
        if char == '[':
            paran_stack.append(idx)


        elif char == ']':
            open_paran_idx = paran_stack.pop()
            if len(paran_stack) == 0:
                start_paran_idx = open_paran_idx
                close_paran_idx = idx

                k = ''
                for i in range(start_paran_idx-1, -1, -1):
                    if s[i].isdigit():
                        k += s[i]
                    else: break
                k = int(k[::-1])

                output += k*decode(s[start_paran_idx+1:close_paran_idx])

        elif not char.isdigit() and len(paran_stack) == 0:
            output += char

    return output


