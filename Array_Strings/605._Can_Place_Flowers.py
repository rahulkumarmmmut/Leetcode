class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        planted = 0
        i = 0

        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1 
                planted += 1
                i += 2  
            else:
                i += 1  

            if planted >= n:
                return True  

        return False 
