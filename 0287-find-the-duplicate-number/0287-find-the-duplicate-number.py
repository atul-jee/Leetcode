class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        arr=[0]*(n+1)
        i=0
        for ele in nums:
            if arr[ele]==0:
                arr[ele]=1
            else:
                return ele
        return 0
