class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        curr=nums[0]
        for i in range(1,len(nums)):
            curr+=nums[i]
            if curr<nums[i]:
                curr=nums[i]
            if max_sum<curr:
                max_sum=curr
            
        return max_sum