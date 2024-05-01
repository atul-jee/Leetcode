class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        l=[]
        for interval in intervals:
            if not l or interval[0]>l[-1][-1]:
                l.append(interval)
            else:
                l[-1][-1]=max(l[-1][-1],interval[-1])
        return l

