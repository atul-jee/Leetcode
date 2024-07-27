class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(arr):
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]
            if n == 2:
                return max(arr[0], arr[1])
            
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
                
            return dp[-1]
        
        l = len(nums)
        if l == 1:
            return nums[0]
        
        # Compare the maximum of robbing the first to second-last or second to last
        return max(helper(nums[1:]), helper(nums[:-1]))

# Example usage:
# solution = Solution()
# print(solution.rob([2, 3, 2]))  # Output: 3
# print(solution.rob([1, 2, 3, 1]))  # Output: 4
# print(solution.rob([1, 2, 3]))  # Output: 3
