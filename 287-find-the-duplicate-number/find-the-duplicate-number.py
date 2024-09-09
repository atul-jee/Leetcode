class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res=[False]*(len(nums))
        for ele in nums:
            if res[ele-1]:
                return ele
            else:
                res[ele-1]=True
        return -1
        