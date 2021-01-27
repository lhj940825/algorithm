class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda word: (-len(word), word))

        for word in words:
            cnt = 0
            for i in range(1, len(word)+1):
                if word[0:i] in words:
                    cnt += 1
                    if cnt == len(word):

                        return word
                else:
                    break



