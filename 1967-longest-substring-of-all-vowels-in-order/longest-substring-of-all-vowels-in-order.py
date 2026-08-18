class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        cur=maxc=vowel=0
        for i in range(0,len(word)):
            if i>0 and word[i]<word[i-1]:
                cur=0
                vowel=0
            cur+=1
            if i==0 or word[i]!=word[i-1]:
                vowel+=1
            if vowel==5:
                maxc=max(maxc,cur)
        return maxc