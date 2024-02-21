from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp = [[0] * n for _ in range(n)]
        dp[-1][-1]=nums[-1]*nums[-2]

        for st in range(n - 2, -1, -1):
            for end in range(st, n):
                mx = -1 * float('inf')
                for i in range(st, end + 1):
                    left = nums[st - 1] if st - 1 >= 0 else 1
                    right = nums[end + 1] if end + 1 < n else 1
                    val = left * right * nums[i]

                    before = dp[st][i - 1] if i - 1 >= st else 0
                    after = dp[i + 1][end] if i + 1 <= end else 0

                    cost = val + before + after
                    mx = max(mx, cost)

                dp[st][end] = mx
        for ele in dp:
            print(ele)
        return dp[0][n - 1]
