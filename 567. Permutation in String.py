class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1map = [0] * 26
        s2map = [0] * 26
        for char in s1:
            s1map[ord(char) - ord('a')] += 1
        for char in s2[:len(s1)]:
            s2map[ord(char) - ord('a')] += 1
        for i in range(len(s2) - len(s1)):
            if self.match(s1map, s2map):
                return True
            s2map[ord(s2[i + len(s1)]) - ord('a')] += 1
            s2map[ord(s2[i]) - ord('a')] -= 1
        return self.match(s1map, s2map)
    
    def match(self, s1map: list, s2map: list) -> bool:
        for i in range(len(s1map)):
            if s1map[i] != s2map[i]:
                return False 
        return True
