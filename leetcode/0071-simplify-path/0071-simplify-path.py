class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        lt = path.split("/")
        for char in lt:
            if char  == "." or char == "":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "/" + "/".join(stack)
            
        
            
