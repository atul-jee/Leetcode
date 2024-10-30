class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        prev=1
        freq=[0]*256
        left=0
        ans=0

        for i in range(len(s)):
            ch=ord(s[i])
            freq[ch]+=1
            while freq[ch]>1:
                freq[ord(s[left])]-=1
                left+=1
            ans=max(ans,i-left+1)
                
        return ans


        
