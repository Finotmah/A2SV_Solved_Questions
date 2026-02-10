class Solution(object):
    def restoreString(self, s, indices):
        shufled_list = [" " for _ in range(len(s))]

        for i, indice in enumerate(indices):
            shufled_list[indice] = s[i]
            
        return "".join(shufled_list)
        
