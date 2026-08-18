class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split()
        word=[]
        for i in range(len(arr)-1,-1,-1):
            word.append(arr[i])
            if i!=0:
               word.append(" ")
        return "".join(word)
