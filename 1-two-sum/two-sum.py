class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        d=defaultdict(int)
        while l<=r and target-nums[l] not in d:
            d[nums[l]]=l
            l+=1
        return [d[target-nums[l]],l]
        