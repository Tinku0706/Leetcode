class Solution:
    def reverseVowels(self, s: str) -> str:
        arr=list(s)
        s=0
        e=len(arr)-1
        st=['a','e','i','o','u','A','E','I','O','U']
        while s<e:
            if arr[s] not in st:
                s+=1
                continue
            if arr[e] not in st:
                e-=1
                continue
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
        return "".join(arr)
            
