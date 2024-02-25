class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        array1 = []
        array2 = []
        for num in nums1:
            if num not in nums2:
                array1.append(num)

        for num in nums2:
            if num not in nums1:
                array2.append(num)
        res1 = list(set(array1))
        res2 = list(set(array2))
        array3 = [res1,res2]
        return array3
                
