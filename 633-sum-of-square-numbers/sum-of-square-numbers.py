class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))
        while (l <= r):
            ans = l**2 + r**2
            if (ans > c):
                r -= 1
            elif (ans < c):
                l += 1
            else:
                return True
        return False