from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutList = []
        for permut in permutations(nums):
            permutList.append(list(permut))
        return permutList
