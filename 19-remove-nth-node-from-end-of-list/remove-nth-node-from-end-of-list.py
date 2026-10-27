class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current=head
        count=0
        while current is not None:
            count+=1
            current=current.next
        target=count-n
        if target==0:
            return head.next
        current=head
        count2=0
        while count2<target-1 is not None:
            current=current.next
            count2+=1
        current.next=current.next.next
       
        return head
            
        