class Solution:
    def removeStars(self, s: str) -> str:
        lists = list(s)
        new_list = []
        for num in s:
            if num == "*":
                new_list.pop(-1)
            elif num != "*":
                new_list.append(num)
        return ''.join(new_list)
