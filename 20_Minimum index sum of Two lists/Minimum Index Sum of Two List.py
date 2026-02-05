class Solution(object):
    def findRestaurant(self, list1, list2):

        list2Dic = {strs: i for i,strs in enumerate(list2)}
        commen_index_string =[]
        min_sum = float('inf')

        for i in range(len(list1)):
            if list1[i] in list2Dic:
                sums = i + list2Dic[list1[i]]
                
                if sums < min_sum:
                    commen_index_string = []
                    commen_index_string.append(list1[i])
                    min_sum = sums

                elif sums == min_sum:
                    commen_index_string.append(list1[i])
                
        return commen_index_string
        
