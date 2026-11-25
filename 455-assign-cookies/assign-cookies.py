class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        left=0
        right=0
        sizeG=len(g)
        sizeS=len(s)
        g.sort()
        s.sort()
        count=0
        while left<sizeG and right<sizeS:
            if g[left]<=s[right]:
                count+=1
                left+=1
                right+=1
            else:
                right+=1
        return count
            
        