class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lists = []
        for num in asteroids:
            while True:
                if not lists or (lists[-1] < 0 and num > 0) or (lists[-1] > 0 and num > 0):
                    lists.append(num)
                    break
                elif lists[-1] < 0 and num < 0:
                    lists.append(num)
                    break
            
                elif abs(lists[-1]) < abs(num):  
                    lists.pop()  
                    if not lists:
                        lists.append(num)
                        break
                elif abs(lists[-1]) == abs(num):  
                    lists.pop()  
                    break
                elif abs(lists[-1]) > abs(num):  
                    break 
        return lists
