# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        st=[]
        slow=head
        fast=head
        while fast and fast.next:
            st.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        mx=0
        while st and slow:
            mx=max(st.pop()+slow.val,mx)
            slow=slow.next
        return mx
        