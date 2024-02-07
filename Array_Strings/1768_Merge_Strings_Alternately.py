class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        shorts = min( len(word1), len(word2))

        for i in range(shorts):
            s = s + word1[i] + word2[i]
        if len(word1) > len(word2):
            s = s + word1[shorts:]
        else:
            s = s + word2[shorts:]
        return s

