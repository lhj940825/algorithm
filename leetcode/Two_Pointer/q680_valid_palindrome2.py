'''
 * Project : algorithm
 * Package : 
 * User    : jun
 * Date    : 2021/02/23
 * Time    : 3:31 오후
'''


class Solution:
    def validPalindrome(self, s: str) -> bool:

        def is_palindrome(s):
            print(s)
            l_pnt, r_pnt = 0, len(s) - 1
            while l_pnt < r_pnt:
                if s[l_pnt] == s[r_pnt]:
                    l_pnt += 1
                    r_pnt -= 1
                else:
                    return False
            return True

        l_pnt = 0
        r_pnt = len(s)-1

        is_char_deleted = False
        while l_pnt < r_pnt:
            if s[l_pnt] == s[r_pnt]:
                l_pnt += 1
                r_pnt -= 1

            else:
                return is_palindrome(s[l_pnt:r_pnt]) or is_palindrome(s[l_pnt+1:r_pnt+1])

        return True




