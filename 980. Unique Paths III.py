from copy import deepcopy

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        # find starting point and count #obstacles
        numObstacles = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    start_row = i
                    start_col = j
                if grid[i][j] == -1:
                    numObstacles += 1
        # count #walkables
        numWalkables = self.m * self.n - numObstacles
        # dfs
        visited = [[0] * self.n for _ in range(self.m)]
        count = self.dfs(start_row, start_col, visited, grid, numWalkables)
        return count
        
    def dfs(self, i, j, visited, grid, numWalkables):
        # if end in the ending point and visited all walkable points
        visited[i][j] = 1
        numWalkables -= 1
        if grid[i][j] == 2 and numWalkables == 0:
            return 1
        c1, c2, c3, c4 = 0, 0, 0, 0
        if i+1 < self.m and grid[i+1][j] != -1 and visited[i+1][j] == 0:
            c1 = self.dfs(i+1, j, deepcopy(visited), grid, numWalkables)            
        if i-1 >= 0 and grid[i-1][j] != -1 and visited[i-1][j] == 0:
            c2 = self.dfs(i-1, j, deepcopy(visited), grid, numWalkables)
        if j+1 < self.n and grid[i][j+1] != -1 and visited[i][j+1] == 0:
            c3 = self.dfs(i, j+1, deepcopy(visited), grid, numWalkables)          
        if j-1 >= 0 and grid[i][j-1] != -1 and visited[i][j-1] == 0:
            c4 = self.dfs(i, j-1, deepcopy(visited), grid, numWalkables)
        return c1 + c2 + c3 + c4
        
