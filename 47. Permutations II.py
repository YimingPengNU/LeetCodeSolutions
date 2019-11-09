from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutUnique = set()
        for permut in permutations(nums):
            if permut not in permutUnique:
                permutUnique.add(permut)
        permutList = []
        for permut in permutUnique:
            permutList.append(list(permut))
        return permutList
        
        
