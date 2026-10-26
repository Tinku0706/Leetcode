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
            current.next=current1 #You're connecting current.next to the entire remaining  linked-list chain, not just one node.so no need to connect each elemnt
        else:
            current.next=current2
        return dummy.next
        
#         1. Suppose these are your linked lists
# list1: 1 → 3 → 5 → 7 → 9
# list2: 2 → 4
# Your while loop compares nodes and merges them until one of the lists becomes None.
# After the loop, the merged list looks like this:
# dummy → 1 → 2 → 3 → 4 → 5
# Remaining nodes in list1:
# 7 → 9
# At this point, current1 points to node 7, and current2 is None.


                

                

        