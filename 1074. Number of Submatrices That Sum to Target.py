from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        res = 0
        row, col = len(matrix), len(matrix[0])
        for k in range(row):
            nums = [0 for _ in range(col)]
            for i in range(k,row):
                for j in range(col):
                    nums[j] += matrix[i][j]
                res += self.check(nums, target)
        return res
    
    def check(self, nums, target):
        counter, res = defaultdict(int), 0
        counter[0], cum_sum = 1, 0
        for num in nums:
            cum_sum += num
            res += counter[cum_sum - target]
            counter[cum_sum] += 1
        return res
