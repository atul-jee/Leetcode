class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        r=len(arr)-k
        while l<r:
            mid=l+(r-l)//2
            if x<=arr[mid]:
                r=mid
            elif arr[mid+k]<=x:
                l=mid+1
            else:
                a=abs(x-arr[mid])
                b=abs(x-arr[mid+k])
                if a<=b:r=mid
                else:l=mid+1
        return arr[l:l+k]
        