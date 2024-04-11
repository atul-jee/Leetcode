class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d=dict()
        for i in range(len(nums)):
            ele=nums[i]
            if ele not in d:
                d[ele]=i
            elif abs(d[ele]-i)<=k:
                    return True
            else:
                d[ele]=i
        return False
        