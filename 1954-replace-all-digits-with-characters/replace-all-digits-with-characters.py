class Solution:
    def replaceDigits(self, s: str) -> str:
        word=[]
        for i in range(0,len(s),2):
            val1=ord(s[i])
            word.append(s[i])
            if i+1<len(s):
              val1 += int(s[i + 1])
              word.append(chr(val1))
        return "".join(word)
    