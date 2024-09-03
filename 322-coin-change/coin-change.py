class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        def helper(arr,ind,target):
            if target==0:
                return 0
            if ind<0 or target<0:
                return 1e9
            if ind==0 :
                if target%arr[ind]==0:
                    return target//arr[ind]
                else:
                    return 1e9
            if dp[ind][target]!=-1:
                return dp[ind][target]
            not_take=helper(arr,ind-1,target)
            take=1e9
            if arr[ind]<=target:
                take=1+helper(arr,ind,target-arr[ind])
            dp[ind][target]=min(take,not_take)
            return dp[ind][target]
        ans=helper(coins,len(coins)-1,amount)
        if ans!=1e9:
            return ans
        return -1