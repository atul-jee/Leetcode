class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev=0
        curr=0
        
        for ele in nums:
            if ele==1:
                curr+=1
            else:
                if prev<curr:
                    prev=curr
                curr=0
        if prev<curr:
            prev=curr
        return prev
        