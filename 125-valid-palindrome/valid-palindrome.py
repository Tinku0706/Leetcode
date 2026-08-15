class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalnum():
                a+=i
        a=a.lower()
        s=0
        e=len(a)-1
        while s<e:
            if a[s]!=a[e]:
                return False
            s+=1
            e-=1
        return True
        