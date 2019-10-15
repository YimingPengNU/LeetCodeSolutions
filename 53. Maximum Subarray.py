class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        partialSum = 0
        partialSumMin = 0
        res = nums[0]
        for i in range(len(nums)):
            partialSum += nums[i]
            res = max(res, partialSum - partialSumMin)
            partialSumMin = min(partialSum, partialSumMin)
        return res
        
