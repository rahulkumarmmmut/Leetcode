# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        max_val = 0
        # for data in listvalue:
        #     head = append1(head,data)
        current = head
        while current:
            stack.append(current.val)
            current = current.next
        for i in range(len(stack)):
            val = stack[i] + stack[-1-i]
            max_val = max(max_val,val)
        return max_val

    def append1(head,data):
        new_node = Node(data)
        if not head:
            return new_node
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head
    
