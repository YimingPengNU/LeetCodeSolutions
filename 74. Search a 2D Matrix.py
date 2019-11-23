class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        # binary search in rows' 1st element
        row_ub = m-1
        row_lb = 0
        while row_ub - row_lb > 1:
            row = (row_ub + row_lb) // 2
            if target > matrix[row][0]:
                row_lb = row
            elif target < matrix[row][0]:
                row_ub = row
            else:
                return True
        if target < matrix[row_ub][0]:
            row = row_lb
        else:
            row = row_ub
        # binary search in matrix[row]
        col_ub = n-1
        col_lb = 0
        if col_ub == col_lb:
            return target == matrix[row][col_lb]
        while col_ub - col_lb > 1:
            col = (col_ub + col_lb) // 2
            if target > matrix[row][col]:
                col_lb = col
            elif target < matrix[row][col]:
                col_ub = col
            else:
                return True
        col = col_lb
        # test if target is found      
        return target == matrix[row][col] or target == matrix[row][col+1]
                
            
            
