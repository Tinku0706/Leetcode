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
    #Store the latest index of a, b, and c in last.
#min(last) gives the leftmost boundary where a valid substring can start while still containing all 3 characters.
#Therefore, there are min(last) + 1 valid substrings ending at the current index, so add it to ans.
            
        