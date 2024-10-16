from typing import Optional
from collections import Counter

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class Solution:
    counts: Counter

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.counts = self.build_counts(head)

        new_head = self.get_next_unique(head)
        last_unique = new_head

        while next := self.get_next_unique(last_unique.next) != None:
            last_unique.next = next
            last_unique = next

        return new_head
    
    def get_next_unique(self, base_node: ListNode):
        node = base_node
        while node != None:
            if self.counts[node.val] > 1:
                node = node.next
            else:
                return node
        
    def build_counts(self, head: ListNode):
        node = head
        values = []

        while node != None:
            values.append(node.val)
            node = node.next
        
        return Counter(values)