class Solution:
    def isPalindrome(self, s: str) -> bool:

        # keep only char such that either alphabet or number
        s = ''.join(list(filter(lambda x: (x>='a' and x <='z') or (x>= 'A'and x<='Z') or x.isdigit(), s)))

        s = s.lower()
        if s == s[::-1]:
            return True
        else: return False