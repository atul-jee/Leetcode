class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=defaultdict()
        st=[]
        for ele in nums2:
            while st and st[-1]<ele:
                d[st.pop()]=ele
            st.append(ele)
        for i in range(len(nums1)):
            
            nums1[i] = d.get(nums1[i], -1)
        print(d)
        return nums1
                