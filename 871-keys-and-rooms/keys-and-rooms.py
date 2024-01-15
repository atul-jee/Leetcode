class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=[False]*(len(rooms))
        #vis[0]=True
        st=[0]
        while st:
            node=st.pop(0)
            vis[node]=True
            for ele in rooms[node]:
                if not vis[ele]:
                    st.append(ele)
        if False in vis:
            return False
        return True