class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance=0
        result=[]
        for i in s:
            if i=='(':
               if balance>0:
                 result.append('(')
               balance+=1
            if i==')':
                balance-=1
                if balance>0:
                    result.append(')')
        return "".join(result)
        