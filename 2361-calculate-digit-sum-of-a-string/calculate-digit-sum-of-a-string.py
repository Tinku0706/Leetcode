class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while(len(s)>k):
            word=[]
            for i in range(0,len(s),k):
                sum=0
                for j in range(i,min(i+k, len(s))):
                    sum+=int(s[j])
                word.append(str(sum))
            s="".join(word)
        return s
                
            

        