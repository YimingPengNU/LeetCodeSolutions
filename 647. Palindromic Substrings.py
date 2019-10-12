class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # base case
        odd = [[i, i] for i in range(len(s))]
        even = [[i, i+1] for i in range(len(s)-1) if s[i]==s[i+1]]
        count = count + len(odd) + len(even)
        for strLen in range(3, len(s)+1):
            if strLen % 2 == 1: # odd
                newOdd = []
                for subStr in odd:
                    left = subStr[0]
                    right = subStr[1]
                    if left > 0 and right < len(s)-1 and s[left-1]==s[right+1]:
                        newOdd.append([left-1, right+1])
                odd = newOdd
                count += len(odd)
            else: # even
                newEven = []
                for subStr in even:
                    left = subStr[0]
                    right = subStr[1]
                    if left > 0 and right < len(s)-1 and s[left-1]==s[right+1]:
                        newEven.append([left-1, right+1])
                even = newEven
                count += len(even)
        return count
        
