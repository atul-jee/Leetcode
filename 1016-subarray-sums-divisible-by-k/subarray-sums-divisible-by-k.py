class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count=0
        curr=0
        d=defaultdict(int)
        d[0]=1
        for ele in nums:
            curr+=ele
            curr=curr%k
            if curr<0:
                curr=curr+ele
            if curr in d:
                count+=d[curr]
            d[curr]+=1
        return count