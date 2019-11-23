class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        # start from matrix[m-1][0]
        pivot_row = m-1
        pivot_col = 0
        while True:
            pivot = matrix[pivot_row][pivot_col]
            if pivot < target:
                pivot_col += 1
                if pivot_col > n-1:
                    return False
            elif pivot > target:
                pivot_row -= 1
                if pivot_row < 0:
                    return False
            else:
                return True
        
