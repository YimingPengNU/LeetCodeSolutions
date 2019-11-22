class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxS = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):  
                if grid[i][j] != 0:
                    maxS = max(maxS, self.dfs(i, j, grid, set()))
        return maxS

    
    def dfs(self, i, j, graph, visited):
        if i >= len(graph) or i < 0 or j >= len(graph[0]) or j < 0:
            return 0
        if (i, j) in visited or graph[i][j] == 0:
            return 0
        visited.add((i,j))
        v = graph[i][j]
        maxV = max(v,
                 v + self.dfs(i, j+1, graph, visited.copy()),
                 v + self.dfs(i, j-1, graph, visited.copy()),
                 v + self.dfs(i-1, j, graph, visited.copy()),
                 v + self.dfs(i+1, j, graph, visited.copy()))
        return maxV
