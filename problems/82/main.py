from typing import Optional

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_unique = head
        first_of_current = head

        while next_different := self.find_next_different(first_of_current) != None:
            # If unique
            if next_different == first_of_current.next:
                last_unique = first_of_current
                first_of_current = next_different
                continue
            # If duplicates detected
            else:
                first_of_current = next_different

    """
    Find next unique node.
    If next_unique != next then prune everything inbetween.
    If next_unique == next then add it and continue
    """

    def find_next_different(base_node: ListNode):
        current = base_node.next
        while current:
            if current.val == base_node.val:
                current = current.next
                continue
            return current
        
