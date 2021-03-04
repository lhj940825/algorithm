'''
 * Project : algorithm
 * Package : 
 * User    : jun
 * Date    : 2021/03/04
 * Time    : 1:00 오후
'''

class Solution:
    def minOperations(self, s: str) -> int:
        odd_items = [int(char) for char in s[1::2]]
        even_items = [int(char) for char in s[0::2]]

        num_one_in_odd = sum(odd_items)
        num_zero_in_odd = len(odd_items)- num_one_in_odd

        num_one_in_even = sum(even_items)
        num_zero_in_even = len(even_items) - num_one_in_even


        cost1 = num_one_in_odd+num_zero_in_even
        cost2 = num_zero_in_odd+num_one_in_even
        return cost1 if cost1<cost2 else cost2


# smarter solution with less space complexity
class Solution:
    def minOperations(self, s: str) -> int:
        answ1=answ0=0
        for i in range(len(s)):
            z=str(i%2)
            answ1+=s[i]!=z
            answ0+=s[i]==z
        return min(answ0,answ1)