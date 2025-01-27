from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def digger(l1: ListNode, l2: ListNode, node: ListNode = ListNode(), rem: int = 0):
            val1 = getattr(l1, "val", 0)
            val2 = getattr(l2, "val", 0)
            
            node =  ListNode(val = val1 + val2 + rem)
            
            if node.val > 9:
                node.val = node.val % 10
                rem = 1
            else:
                rem = 0

            if (
                getattr(l1, "next", None) is None and
                getattr(l2, "next", None) is None
            ):
                if rem:
                    node.next = ListNode(val=rem)
                return node

            node.next = digger(getattr(l1, "next", None), getattr(l2, "next", None), node, rem)
            return node
        return digger(l1, l2)
