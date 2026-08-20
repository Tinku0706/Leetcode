class Solution:
    def frequencySort(self, s: str) -> str:
        word=[]
        mp=Counter(s)
        for key,value in sorted(mp.items(),key=lambda x:x[1],reverse=True):
            val=value
            while val>0:
               word.append(key)
               val-=1
        return "".join(word)
        