class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen=[-1,-1,-1]
        ans=0
        for i,ch in enumerate(s):
            if ch=='a':
                lastseen[0]=i
            elif ch=='b':
                lastseen[1]=i
            else:
                lastseen[2]=i
            ans+=min(lastseen)+1
        return ans
            
        