class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        news = list(s)
        newt = list(t)

        if len(news) == 0:
            return True
        else:
            j = 0
            for i in range(len(newt)):
                if j < len(news) and news[j] == newt[i]:
                    j += 1

            if j == len(news):
                return True
            else:
                return False
