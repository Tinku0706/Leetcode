class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        current=head
        count=0
        while current is not None:
            count+=1
            current=current.next
        middle_elmt=(count//2)
        current=head
        count2=0
        while current is not None:
            if count2 == middle_elmt:
                return current
            count2 += 1
            current = current.next
        return None



        