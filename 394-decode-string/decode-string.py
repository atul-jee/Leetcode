class Solution:
    def decodeString(self, s: str) -> str:
        
        cur_num=0
        st=[]
        cur_ele=''
        for ele in s:
            if ele=='[':
                st.append([cur_ele,cur_num])
                cur_ele,cur_num='',0
            elif ele==']':
                a,b=st.pop()
                cur_ele=a+b*cur_ele
            elif ele.isdigit():
                cur_num=cur_num*10+int(ele)
            else:
                cur_ele+=ele
        return cur_ele
            


