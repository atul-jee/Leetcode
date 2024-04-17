class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        mx=0
        for ele in boxTypes:
            if ele[0]>=truckSize:
                mx+=(truckSize*ele[1])
                break
                
            else:
                mx+=(ele[0]*ele[1])
                truckSize-=ele[0]
                
        return mx
        
        