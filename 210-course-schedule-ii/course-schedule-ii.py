class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> bool:
        g={i:[] for i in range(n)}
        indegree=[0]*n
        for u,v in pre:
            g[v].append(u)
            indegree[u]+=1
        q=deque()
        for i in range(n):
            if indegree[i]==0:q.append(i)
        course=[0]*n
        i=0
        while q:
            u=q.popleft()
            course[i]=u
            i+=1

            for neigh in g[u]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if i!=n:return []
        return course
        
        
