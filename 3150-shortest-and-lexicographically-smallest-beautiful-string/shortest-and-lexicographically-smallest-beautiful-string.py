class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        minc=float('inf')
        minw=""
        for i in range(len(s)):
            count=0
            for j in range(i,len(s)):
                if s[j]=='1':
                    count+=1
                if count==k:
                    size=j-i+1
                    curr=s[i:j+1]
                    if size<minc or (size == minc and curr < minw):
                        minc=size
                        minw=s[i:j+1]
                        break
        return minw


        