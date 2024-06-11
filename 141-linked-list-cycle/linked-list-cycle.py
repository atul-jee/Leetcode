# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d=defaultdict(int)
        temp=head
        while temp:
            if d[temp]>0:
                return True
            else:
                d[temp]+=1
            temp=temp.next
        return False
        