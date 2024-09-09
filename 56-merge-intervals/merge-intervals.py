class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr=[]
        i=0
        for u in intervals:
            if len(arr)==0 or arr[-1][-1]<u[0]:
                arr.append(u)
            else:
                arr[-1][-1]=max(arr[-1][-1],u[-1])
        return arr
        