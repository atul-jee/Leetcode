class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        for i in range(1,len(prices)):
            mx+=(prices[i]-prices[i-1]) if prices[i]>prices[i-1] else 0
        return mx

        