class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        mx=0
        for u,v in boxTypes:
            if u>=truckSize:
                mx+=(truckSize*v)
                break
                
            else:
                mx+=(u*v)
                truckSize-=u
                
        return mx
        
        