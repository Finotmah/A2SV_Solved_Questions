class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        res = []
        visited = set([s])
        queue = deque([s])
        found = False

        while queue:
            curr = queue.popleft()
            if is_valid(curr):
                res.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in '()':
                    continue
                
                next_str = curr[:i] + curr[i+1:]
                
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
        return res

    