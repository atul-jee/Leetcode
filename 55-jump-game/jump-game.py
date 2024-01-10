class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr=0
        for i in range(len(nums)):
            if i>curr:
                return False
            curr=max(curr,nums[i]+i)
            if curr>=len(nums)-1:
                return True
        return False
        