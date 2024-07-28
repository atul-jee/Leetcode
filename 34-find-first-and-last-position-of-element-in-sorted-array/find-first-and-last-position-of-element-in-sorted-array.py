class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        first=-1
        while l<=r:
            mid=(r-l)//2+l
            if nums[mid]==target:
                first=mid
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        l=0
        r=len(nums)-1
        second=-1
        while l<=r:
            mid=(r-l)//2+l
            if nums[mid]==target:
                second=mid
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return [first,second]
        
        