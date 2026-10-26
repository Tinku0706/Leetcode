class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        current1=list1
        current2=list2
        dummy=ListNode(-1)
        current=dummy
        while current1 is not None and current2 is not None:
            if current1.val<=current2.val:
                current.next=current1
                current1=current1.next
            else:
                current.next=current2
                current2=current2.next
            current=current.next
            
        if current1 is not None:
            current.next=current1
        else:
            current.next=current2
        return dummy.next
        


                

                

        