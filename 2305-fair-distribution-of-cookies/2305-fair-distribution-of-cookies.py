class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        children = [0] * k
        self.ans = float('inf')

        def backtrack(i):
            # all cookies assigned
            if i == len(cookies):
                self.ans = min(self.ans, max(children))
                return

            # pruning: already worse than best
            if max(children) >= self.ans:
                return

            seen = set()

            for j in range(k):
                if children[j] in seen:
                    continue
                seen.add(children[j])

                children[j] += cookies[i]
                backtrack(i + 1)
                children[j] -= cookies[i]

        backtrack(0)
        return self.ans