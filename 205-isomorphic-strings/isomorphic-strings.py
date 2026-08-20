class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1={}#mp1 asks:What character does this s character map to?
        mp2={}   #mp2 asks: Has this t character already been taken by another s character?
        for x,y in zip(s,t):  #takes e from s and a from t string (e,a)then(g,d)
            if x in mp1 and mp1[x]!=y:
                return False
            if y in mp2 and mp2[y]!=x:
                return False
            mp1[x]=y
            mp2[y]=x
        return True
    
     