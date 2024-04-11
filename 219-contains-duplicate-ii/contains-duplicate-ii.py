class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range(len(nums)):
            ele=nums[i]
            if ele in d:
                if abs(d[ele]-i)<=k:
                    return True
                else:
                    d[ele]=i
            else:
                d[ele]=i
        return False
        