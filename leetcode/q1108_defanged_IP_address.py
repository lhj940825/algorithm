'''
 * User: Hojun Lim
 * Date: 2020-12-31
'''
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.', '[.]')
        return address
