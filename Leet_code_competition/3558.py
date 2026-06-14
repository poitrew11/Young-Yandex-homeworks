class Solution:
    MODE = 10**9 + 7

    def dfs(self, g: List[List[int]], x: int, fa: int) -> int:
        max_depth = 0
        for y in g[x]:
            if y == fa:
                continue
            max_depth = max(max_depth, self.dfs(g, y, x) + 1)
        return max_depth

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        max_depth = self.dfs(graph, 1, 0)
        ans = pow(2, max_depth -1, self.MODE)
        return ans
