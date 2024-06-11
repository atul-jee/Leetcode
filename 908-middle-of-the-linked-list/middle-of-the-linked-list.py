# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        count=1
        slow=head
        while head:
            if (count & 1 )== 0:
                slow=slow.next
            head=head.next
            count+=1
        return slow

        