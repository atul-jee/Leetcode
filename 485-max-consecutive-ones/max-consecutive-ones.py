class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev=0
        curr=0
        
        for ele in nums:
            curr+=ele
            if ele==0:
                if prev<curr:
                    prev=curr
                curr=0
        if prev<curr:
            prev=curr
        return prev
        