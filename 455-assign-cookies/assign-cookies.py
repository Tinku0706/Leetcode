class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        i=0
        j=0
        g.sort()
        s.sort()
        count=0
        g_size=len(g)
        s_size=len(s)
        while i<g_size and j<s_size:
            if s[j]>=g[i]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count

        