class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(len(nums)):
            if target - nums[i] in complement:
                return [complement[target - nums[i]], i]
            complement[nums[i]] = i
