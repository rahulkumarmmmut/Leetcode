class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        rightp = 0
        leftp = 0
        max_length = 0
        countZero = 0

        while rightp < len(nums):
            if nums[rightp] == 0:
                countZero += 1
            while countZero > 1:
                if nums[leftp] == 0:
                    countZero -= 1
                leftp += 1
            max_length = max(max_length, rightp - leftp)
            rightp += 1

        return max_length
