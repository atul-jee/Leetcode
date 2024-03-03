class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            cur=nums[i]
            l=i+1
            r=n-1
            while l<r:
                target=cur+nums[l]+nums[r]
                if target==0:
                    ans.append([cur,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<n and l<r and nums[l]==nums[l-1]:
                        l+=1
                    while r>0 and l<r and nums[r]==nums[r+1]:
                        r-=1
                    
                elif target<0:
                    l+=1
                else:
                    r-=1
                    
            
        return ans

        