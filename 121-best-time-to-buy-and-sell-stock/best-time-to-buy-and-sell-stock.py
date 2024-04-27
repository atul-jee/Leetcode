class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=float('-inf')
        price=prices[0]
        for ele in prices:
            price=min(price,ele)
            profit=max(profit,ele-price)
        return profit

        