class Solution:
    def checkValidString(self, s: str) -> bool:
        
        min=max=0
        for i in s:
            if i=='(':
                min=min+1
                max=max+1
            elif i==')':
                min=min-1
                max=max-1
            else:
                min=min-1
                max=max+1
            
            if min<0:
                min=0
            if max<0:
                return False
        return min==0