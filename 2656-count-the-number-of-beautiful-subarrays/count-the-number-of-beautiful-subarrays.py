class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        d=defaultdict(int)
        d[0]=1
        xor=0
        count=0
        for ele in nums:
            xor^=ele
            count+=d[xor]
            d[xor]+=1
        return count

