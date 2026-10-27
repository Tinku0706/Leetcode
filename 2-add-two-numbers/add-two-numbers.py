class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
       dummy=ListNode(0)
       current=dummy
       carry=0
       while l1 is not None or l2 is not None or carry:
          num1=l1.val if l1 is not None else 0
          num2=l2.val if l2 is not None else 0

          total=num1+num2+carry
          carry=total//10
          digit=total%10

          current.next=ListNode(digit)
          current=current.next

          if l1 is not None:
            l1=l1.next
          if l2 is not None:
            l2=l2.next
       return dummy.next
