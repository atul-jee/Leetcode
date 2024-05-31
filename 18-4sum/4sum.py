class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-3):
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                h=n-1
                curr_target=target-(nums[i]+nums[j])
                while l<h:
                    if l>j+1 and nums[l]==nums[l-1]:
                        l+=1
                        continue
                    if h<n-1 and nums[h]==nums[h+1]:
                        h-=1
                        continue
                    curr_sum=nums[l]+nums[h]
                    if curr_sum<curr_target:
                        l+=1
                    elif curr_sum>curr_target:
                        h-=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[h]])
                        l+=1
                        h-=1
        return res
