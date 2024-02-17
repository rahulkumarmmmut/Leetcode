from typing import List
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count_map = defaultdict(int) 
        operations = 0
        
        for num in nums:
            complement = k - num  
            if count_map[complement] > 0: 
                operations += 1
                count_map[complement] -= 1  
            else:
                count_map[num] += 1  
        
        return operations
