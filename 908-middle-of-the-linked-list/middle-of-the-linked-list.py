class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
# How it works
# Suppose the linked list is:

# 1 → 2 → 3 → 4 → 5 → None
# - slow moves one node at a time.
# - fast moves two nodes at a time.
# - When fast reaches the end, slow is at the middle.



        