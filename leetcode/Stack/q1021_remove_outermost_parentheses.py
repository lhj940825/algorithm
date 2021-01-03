'''
 * User: Hojun Lim
 * Date: 2021-01-04
'''
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        open_parentheses = []

        output = ''
        for char in S:
            if char == '(':
                open_parentheses.append(char)
                if len(open_parentheses) > 1:
                    output += '('

            if char == ')':
                if len(open_parentheses) > 1:
                    output += ')'
                open_parentheses.pop()


        return output


