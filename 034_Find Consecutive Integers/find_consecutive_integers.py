import math
class Solution(object):
    def sumOfThree(self, num):
        result = []
        x = (num + 3)/3.0
        if x - math.floor(x) == 0:
            x = int(x)
            result.extend([x -2, x -1, x])


        return result


        
