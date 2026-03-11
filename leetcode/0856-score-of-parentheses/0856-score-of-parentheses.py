class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        stack = []
        
        for c in s:
            if c == ')':
                if stack and stack[-1] == "(":
                    score = 1
                    stack.pop()
                    stack.append(score)
                    score = 0
                else:
                    score = stack.pop()
                    while stack and stack[-1] != '(':
                        score += stack.pop()
                    
                    stack.pop()
                    score *= 2
                    stack.append(score)
            else:
                stack.append(c)

        return sum(stack)
                    


