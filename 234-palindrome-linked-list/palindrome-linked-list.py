class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if head is None or head.next is None:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        current=slow

        while current:
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode

        left=head
        right=prev

        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True
        
           