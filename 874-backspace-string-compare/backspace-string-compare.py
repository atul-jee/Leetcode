class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(string):
            st=[]
            for ele in string:
                if ele=='#':
                    if st:
                        st.pop()
                else:
                    st.append(ele)
            return st
        a=helper(s)
        b=helper(t)
        #print(a,b)
        return a==b
                
        