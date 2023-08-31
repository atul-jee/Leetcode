def binary(arr,k):
    l=0
    r=len(arr)
    while l<r:
        mid=(l+r)//2
        if arr[mid]<k:
            l=mid+1
        else:
            r=mid
    return l
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        _1st= binary(nums,target)
        _2nd= binary(nums,target+1)-1
        if _1st<=_2nd:
            return [_1st,_2nd]
        return [-1,-1]