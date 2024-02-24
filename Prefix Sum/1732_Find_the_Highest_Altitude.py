class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pos = 0
        max_pos = pos
        for i in range(len(gain)):
            pos = pos + gain[i]
            max_pos = max( pos, max_pos)
        return max_pos
