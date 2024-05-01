from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=defaultdict(int)
        for ele in nums1:
            d[ele]=1
        l=[]
        for ele in d.keys():
            if ele in nums2:
                l.append(ele)
            
        return l
