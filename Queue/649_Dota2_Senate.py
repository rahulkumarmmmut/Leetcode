class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        Radiant = deque()
        Dire = deque()

        for i, senator in enumerate(senate):
            if senator == "R":
                Radiant.append(i)
            else:
                Dire.append(i)
        n = len(senate)

        while Radiant and Dire:
            r = Radiant.popleft()
            d = Dire.popleft()

            if r < d:
                Radiant.append(n+r)
            else:
                Dire.append(n+d)

        if Radiant:
            return "Radiant"
        else:
            return "Dire"
