class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ')
        words.reverse()
        ret = ''    
        for w in words:
            w.strip() 
            if w:
                ret += w
                ret += ' '
        return ret.strip()
