class Solution:
    def simplifyPath(self, path):
        ans=[]
        path=path.split('/')
        for ele in path:
            if ans and ele=="..":
                ans.pop()
            elif ele not in ["",".",".."]:
                ans.append(ele)
        return "/"+"/".join(ans)