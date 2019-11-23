class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= k+1:
            return len(set(nums)) < len(nums)
        
        window = set(nums[:(k+1)])
        if len(window) < k+1:
            return True
        for i in range(1, len(nums)-k):
            window.remove(nums[i-1])
            window.add(nums[i+k])
            if len(window) < k+1:
                return True
        return False
        
