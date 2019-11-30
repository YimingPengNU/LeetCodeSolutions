class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.placeQueens(n)
    
    def placeQueens(self, n, r=0, Q=None, res=[]):
        if not Q: 
            Q, res = [0] * n, []
        if r == n:
            res.append(['.' * j + 'Q' + '.' * (n - j - 1) for j in Q])
            return
        for j in range(n):
            legal = True
            for i in range(r):
                if Q[i] == j or Q[i] == j+r-i or Q[i] == j-r+i:
                    legal = False
            if legal:
                Q[r] = j
                self.placeQueens(n, r+1, Q, res)
        return res
