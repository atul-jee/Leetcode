class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def longest(l, r):
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
            
            return s[l+1:r]
        
        res = ""
        for i in range(n):
            res = max(res, longest(i,i), longest(i,i+1),key=len)
        


        return res