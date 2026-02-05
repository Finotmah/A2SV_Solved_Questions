class Solution(object):
    def removeComments(self, source):
        result = []
        flag = False 
        strs = ""     
        
        for s in source:
            
            i = 0
            while i < len(s):
               
                if flag:
                    if i + 1 < len(s) and s[i] == '*' and s[i+1] == '/':
                        flag = False 
                        i += 1  
                            
                else:
                    if i + 1 < len(s) and s[i] == '/' and s[i+1] == '*':
                        flag = True
                        i += 1       
                    elif i + 1 < len(s) and s[i] == '/' and s[i+1] == '/':
                        break        
                    else:
                        strs += s[i]
                i += 1
            
            
            if not flag and strs:
                result.append(strs)
                strs = "" 
        return result
