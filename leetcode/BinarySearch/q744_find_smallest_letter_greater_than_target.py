# Binary Search solution
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:


        smallest_idx = bin_search(0, len(letters)-1, target, letters)
        if smallest_idx == len(letters):
            smallest_idx = 0

        return letters[smallest_idx]

def bin_search(start, end , target, _list):
    if start > end:
        return start

    mid = (start+end)//2
    cur_val = _list[mid]

    if cur_val > target:
        return bin_search(start, mid-1, target, _list)
    else:
        return bin_search(mid+1, end, target, _list)



# Brute force


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        seen = []
        for letter in letters:
            if letter in seen:
                continue
            else:
                seen.append(letter)
        letters = seen

        i = 0
        for letter in letters:
            if letter <= target:
                i+= 1
                if i == len(letters):
                    return letters[0]
                else:
                    continue
            else:
                return letter
