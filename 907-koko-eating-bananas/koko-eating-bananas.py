class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(rate):
            count=0
            for p in piles:
                count+=math.ceil(p/rate)
            return count<=h
        l=1
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            if valid(mid):
                r=mid
            else:
                l=mid+1
        return l

