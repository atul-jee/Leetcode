class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev=0
        curr=0
        
        for ele in nums:
            if ele==1:
                curr+=1
            else:
                prev=max(prev,curr)
                curr=0
        return max(curr,prev)
        