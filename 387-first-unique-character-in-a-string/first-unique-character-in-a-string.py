class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp=Counter(s)
        for i in range(0,len(s)):
            if mp[s[i]]==1:
                return i

        return -1
        