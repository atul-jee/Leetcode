class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        _1st=-1
        _2nd=-1
        for i in range(len(nums)):
            if nums[i]==target:
                _1st=i
                break
        for j in range(len(nums)-1,-1,-1):
            if nums[j]==target:
                _2nd=j
                break
        return [_1st,_2nd]