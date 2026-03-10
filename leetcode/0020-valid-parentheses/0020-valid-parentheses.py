class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mymap = {'}':'{',']':'[',')':'('}

        for br in s:
            if br not in mymap:
                stack.append(br)
            else:
                if not stack:
                    return False
                if stack[-1] != mymap[br]:
                    return False
                else:
                    stack.pop()
        return not stack