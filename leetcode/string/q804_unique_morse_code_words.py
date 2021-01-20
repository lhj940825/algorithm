'''
 * User: Hojun Lim
 * Date: 2021-01-19
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_dic = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_codes = []
        for word in words:
            morse_code = ''
            for char in word:
                morse_code_idx = ord(char) - 97
                morse_code += morse_code_dic[morse_code_idx]
            morse_codes.append(morse_code)

        morse_codes = set(morse_codes)
        return len(morse_codes)

