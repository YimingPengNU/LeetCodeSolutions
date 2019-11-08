import numpy as np

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid = np.asarray(grid)
        rowMax = grid.max(axis=1)
        colMax = grid.max(axis=0)
        sumMax = 0
        for i in range(len(rowMax)):
            for j in range(len(colMax)):
                sumMax += min(rowMax[i], colMax[j])
        return sumMax - grid.sum()
        
