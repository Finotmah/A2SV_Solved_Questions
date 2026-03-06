# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre = None 
        curr = head

        while curr:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        
        return pre