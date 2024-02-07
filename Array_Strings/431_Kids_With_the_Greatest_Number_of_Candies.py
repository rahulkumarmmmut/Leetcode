class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = []
        x =  len(candies)
        maxi = 0

      
        maxi = max(candies)

        for i in range(x):
            m =  candies[i] + extraCandies
            if m >= maxi:
                a.append(True)
            else:
                a.append(False)
        return a
        



        
