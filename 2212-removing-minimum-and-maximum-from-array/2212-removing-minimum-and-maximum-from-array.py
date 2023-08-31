class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn=min(nums)
        mx=max(nums)
        n=len(nums)
        x=nums.index(mn)+1
        y=nums.index(mx)+1
        ans1= min(max(n-x+1,n-y+1),max(x,y))
        if x>y:
            x,y=y,x
        ans2=x+(n-y)+1
        res=min(ans1,ans2)
        return res if n>2 else n
        
    
