class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for i in range(low, high + 1):
            s = str(i)
            if len(s) % 2 == 0:
                n = len(s) // 2
                a = int(s[:n])
                b = int(s[n:])

                s1, s2 = 0, 0

                
                while a:
                    s1 += a % 10
                    a //= 10

                while b:
                    s2 += b % 10
                    b //= 10

                # Compare the sums
                if s1 == s2:
                    ans += 1

        return ans

