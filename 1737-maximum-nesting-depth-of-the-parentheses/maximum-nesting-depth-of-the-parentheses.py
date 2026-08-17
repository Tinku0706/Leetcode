class Solution:
    def maxDepth(self, s: str) -> int:
        ans=res=0
        for i in s:
            if i=='(':
                ans+=1
                res=max(res,ans)
            elif i==')':
                ans-=1
        return res
            
        