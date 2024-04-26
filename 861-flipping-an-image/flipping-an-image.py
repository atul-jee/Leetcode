class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def reverse(arr):
            l=0
            r=len(arr)-1
            while l<r:
                arr[l],arr[r]=arr[r]^1,arr[l]^1
                l+=1
                r-=1
            if len(arr)%2:
                arr[l]=arr[l]^1
            return arr
        for i in range(len(image)):
            image[i]=reverse(image[i])
        return image
        