'''
 * User: Hojun Lim
 * Date: 2020-12-31
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()

        half_idx = len(s)//2
        a = s[:half_idx]
        b = s[half_idx:]

        num_vowel_a, num_vowel_b = 0, 0
        for i in range(half_idx):
            if a[i] in ['a','e','i','o','u']:
                num_vowel_a += 1

            if b[i] in ['a','e','i','o','u']:
                num_vowel_b += 1


        if num_vowel_a == num_vowel_b:
            return True
        return False