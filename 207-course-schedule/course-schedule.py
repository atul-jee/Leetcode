class Solution:
    def canFinish(self, n: int, pre: List[List[int]]) -> bool:
        g={i:[] for i in range(n)}
        indegree=[0]*n
        for u,v in pre:
            g[u].append(v)
            indegree[v]+=1
        q=[]
        count=0
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
                indegree[i]=-1
        while q:
            u=q.pop(0)
            count+=1
            for neigh in g[u]:
                if indegree[neigh]!=-1:
                    indegree[neigh]-=1
                    if indegree[neigh]==0:
                        q.append(neigh)
                        indegree[neigh]=-1
        return count==n
        
        
