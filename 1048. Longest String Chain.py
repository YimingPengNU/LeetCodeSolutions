class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordsSorted = sorted(words, key=len)
        dpTable = [1] * len(words)
        for i in range(1, len(dpTable)):
            curr = wordsSorted[i]
            preOpt = 0
            j = i
            while j > 0:
                j -= 1
                pre = wordsSorted[j]
                if self.isPred(pre, curr):
                    preOpt = dpTable[j]
                    if preOpt + 1 > dpTable[i]:
                        dpTable[i] = preOpt + 1
                    
        return max(dpTable)
                
                
    def isPred(self, word1, word2):
        # base case
        if len(word1) == 0:
            return True
        
        if len(word1) + 1 == len(word2):
            if word1[0] == word2[0]:
                return self.isPred(word1[1:], word2[1:])
            else:
                return word1 == word2[1:]
        else:
            return False
        
                
            
            
