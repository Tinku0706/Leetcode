class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        current=head
        nums=[]
        while current is not None:
            nums.append(current.val)
            current=current.next
        return nums==nums[::-1]
        
           