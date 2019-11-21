class Solution:
    def countBits(self, num: int) -> List[int]:
        if num <= 1:
            return list(range(num+1))
        # num >= 2
        res = [0] * (num + 1)
        res[0:2] = [0, 1]
        powerOfTwo = 1
        while powerOfTwo * 2 <= num:
            res[powerOfTwo * 2] = 1
            for i in range(powerOfTwo + 1, powerOfTwo * 2):
                res[i] = res[powerOfTwo] + res[i - powerOfTwo]
            powerOfTwo *= 2
        for i in range(powerOfTwo + 1, num + 1):
            res[i] = res[powerOfTwo] + res[i - powerOfTwo]
        return res
