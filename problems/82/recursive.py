from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_unique = head


    def find_next_unique(self, base_node: ListNode):
        next_different = self.find_next_different(base_node)
        
        if next_different == base_node.next:
            
        
    def find_next_different(self, base_node: ListNode):
        current = base_node.next
        while current:
            if current.val == base_node.val:
                current = current.next
                continue
            return current
        