class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        d=defaultdict(int)
        d[0]=1
        curr=0
        for ele in nums:
            curr+=ele%2
            if curr-k in d:
                count+=d[curr-k]
            d[curr]+=1
        return count