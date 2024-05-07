class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        m=1
        j=len(nums)-1
        while m<=j:
            if nums[i]==0:
                if nums[m]!=0:
                    nums[i],nums[m]=nums[m],nums[i]
                    i+=1
                m+=1
            else:
                i+=1
                m+=1
        

