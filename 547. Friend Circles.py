class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # DFS approach
        N = len(M)
        visited = [False] * N
        count = 0
        for i in range(N):
            if visited[i]:
                continue
            count += 1
            self.dfs(M, i, visited)            
        return count
            
    def dfs(self, M, i, visited):
        visited[i] = True
        for j in range(len(M[i])):
            if M[i][j] == 1 and not visited[j]:
                self.dfs(M, j, visited)
     
