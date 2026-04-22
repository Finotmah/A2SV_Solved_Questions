class Solution:
    from collections import defaultdict
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(s,v):
            if s == destination:
                return True
            v.add(s)

            for adj in graph[s]:

                if adj not in v:
                    if dfs(adj,v):
                        return True
            return False


        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        return dfs(source,visited)
        