class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 0
        total = sum(nums[:k])
        maxtotal = total
        for i in range(len(nums)-k):
            total = total - nums[i]
            total = total + nums[i+k]
            maxtotal = max(maxtotal,total)
        x = float((maxtotal)/k)
        return x
        
