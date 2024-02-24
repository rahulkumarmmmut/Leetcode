class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0 
        pivot_index = -1  

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum: 
                pivot_index = i  
                break 
            left_sum += nums[i]  

        return pivot_index
                
