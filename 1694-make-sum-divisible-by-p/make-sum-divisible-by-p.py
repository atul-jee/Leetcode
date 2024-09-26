class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s=sum(nums)
        if s%p==0:
            return 0
        k=s%p
        def helper(arr,k,p):
            d={}
            d[0]=-1
            curr=0
            mx=len(arr)
            for i in range(len(arr)):
                curr=(curr+arr[i])%p
                if (curr-k)%p in d:
                    mx=min(mx,i-d[(curr-k)%p])
                d[curr]=i
            return mx
        ans=helper(nums,k,p)
        if ans>=len(nums):
            return -1
        return ans