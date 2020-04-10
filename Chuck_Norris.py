'''
 * User: Hojun Lim
 * Date: 2020-04-09
'''

import sys
import math

def ascii2binary(input):
    decimal = ord(input) # return ascii code of input

    binary = ''
    while decimal > 0:
        binary+= str(decimal%2) # decimal%2 = remainder
        decimal = decimal //2 # // operator discard the remainder and only take the integer

    if len(binary) < 7: # when the generated binary code is not 7-bit
        temp = ['0' for i in range(7-len(binary))]
        temp = ''.join(temp)
        binary = binary + temp

    return binary[::-1] #return the binary in reverse order


message = input()

binary_string = ""
for ch in message:
    ascii_ch = ascii2binary(ch)
    binary_string+=ascii_ch
#print(binary_string)

previous_bit = ''
cyper = '' # encoded binary_string
code_book= {'1':' 0 ', '0':' 00 '}

for bit in binary_string:
    if previous_bit != bit:
        cyper += code_book[bit]

    cyper += '0'

    previous_bit = bit

print(cyper[1:])
