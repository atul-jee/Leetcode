class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_sum=0
        ans=max(0,gain[0])
        for i in range(1,len(gain)):
            gain[i]=gain[i]+gain[i-1]
            ans=max(ans,gain[i])
        return ans


        