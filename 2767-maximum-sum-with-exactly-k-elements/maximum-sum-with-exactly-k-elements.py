class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m=0
        s=max(nums)
        for i in range(k):
            m+=s
            s=s+1
        return m
        