'''
 * User: Hojun Lim
 * Date: 2020-12-17
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ''.join(word1)
        str2 = ''.join(word2)

        if str1 == str2:
            return True
        return False