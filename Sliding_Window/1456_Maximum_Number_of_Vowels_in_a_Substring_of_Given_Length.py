class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sub_array = ["a", "e", "i", "o", "u"]
        lists = list(s)
        total = 0
        maxtotal = 0
        for i in range(k):
            if lists[i] in sub_array:
                total += 1
        maxtotal = total
        for i in range(1, len(lists) - k + 1):
            if lists[i - 1] in sub_array:
                total -= 1
            if lists[i + k - 1] in sub_array:
                total += 1
            maxtotal = max(maxtotal, total)
        return maxtotal
