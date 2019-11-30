class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # sort by 2nd #
        pairs = sorted(pairs, key=lambda x: x[1])
        last, res = float("-inf"), 0
        for pair in pairs:
            if last < pair[0]:
                res += 1
                last = pair[1]
        return res
