class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        digit=start ^ goal
        count=0
        while digit>0:
            lastd=digit&1
            if lastd==1:
                count+=1
            digit>>=1
        return count
        