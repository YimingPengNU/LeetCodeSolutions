class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # DFS approach
        N = len(M)
        nodes_visited = [False] * N
        count = 0
        for i in range(N):
            if not nodes_visited[i]:
                count += 1
                stack = [i]
                while len(stack) > 0:
                    curr = stack.pop()
                    nodes_visited[curr]  = True
                    adj_list = [index for index, item in enumerate(M[curr]) if item != 0 and not nodes_visited[index]]
                    stack.extend(adj_list)
                
        return count
                    
            
