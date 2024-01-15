class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=[False]*(len(rooms))
        #vis[0]=True
        def dfs(node):
            #nonlocal vis,rooms
            vis[node]=True
            for ele in rooms[node]:
                if not vis[ele]:
                    dfs(ele)
        dfs(0)
        if False in vis:
            return False
        return True
                
        