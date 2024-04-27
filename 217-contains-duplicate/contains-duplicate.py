from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=defaultdict(int)
        for ele in nums:
            if d[ele]>0:
                return True
            d[ele]+=1
        return False

        