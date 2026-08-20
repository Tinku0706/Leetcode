class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxw=""
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        for i in range(len(s)):
            word1=expand(i,i)
            word2=expand(i,i+1)
            if len(word1)>len(maxw):
                maxw=word1
            if len(word2)>len(maxw):
                maxw=word2
        return maxw