class Solution:
    def reverseWords(self, s: str) -> str:
        st=''
        w=''
        n=len(s)
        for i in range(n):
            if s[i]==' ':
                if i>0 and s[i-1]!=s[i]:
                    st=(w+' ')+st
                    w=''
            else:
                w+=s[i]
        return (w+' '+st).strip()