class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dpTable = {}
        for w in sorted(words, key=len):
            dpTable[w] = max(dpTable.get(w[:i] + w[i+1:], 0) + 1 for i in range(len(w)))      
        return max(dpTable.values())
            
