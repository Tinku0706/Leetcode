class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans=-1
        res=[]
        for i in range(len(num)-1,-1,-1):
            a=int(num[i])
            if a%2!=0:
                ans=i
                break
        for i in range(0,ans+1):
            res.append(num[i])
        return "".join(res)
        
        