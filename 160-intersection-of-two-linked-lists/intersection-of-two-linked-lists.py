class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA=headA
        pB=headB
        while pA!=pB:
            if pA is None:
                pA=headB
            else:
                pA=pA.next
            if pB is None:
                pB=headA
            else:
                pB=pB.next
        return pA
            


        