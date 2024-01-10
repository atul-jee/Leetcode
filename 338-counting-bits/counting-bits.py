class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [0]
        ans=[0]*(n+1)
        ans[1]=1
        for i in range(2,n+1):
            if i%2:
                ans[i]=ans[i//2]+1
            else:
                ans[i]=ans[i//2]
        return ans

        