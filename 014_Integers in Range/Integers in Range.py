class Solution(object):
    def isCovered(self, ranges, left, right):

        flag  = False
        for i in range(left, right + 1):
            flag = False

            for j in range(len(ranges)):
                if i >= ranges[j][0] and i <= ranges[j][1]:
                    flag = True
                    break
                
            if not flag:
                return False
            
        return flag


        