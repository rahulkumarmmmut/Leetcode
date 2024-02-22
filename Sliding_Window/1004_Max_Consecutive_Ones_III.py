class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        leftp = 0
        rightp = 0
        zeroCount = 0
        maxLen = 0
        maximum = 0

        for rightp in range(len(nums)):
            if nums[rightp] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[leftp] == 0:
                    zeroCount -= 1
                leftp += 1
            maxLen = rightp - leftp + 1
            maximum = max(maxLen, maximum)

        return maximum
