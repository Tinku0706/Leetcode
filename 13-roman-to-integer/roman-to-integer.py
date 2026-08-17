class Solution:
    def romanToInt(self, s: str) -> int:
        mp={}
        mp["I"]=1
        mp["V"]=5
        mp["X"]=10
        mp["L"]=50
        mp["C"]=100
        mp["D"]=500
        mp["M"]=1000
        i=sum=0
        j=len(s)
        while i<j:
            val1=mp[s[i]]
            if i+1<j:
                val2=mp[s[i+1]]
                if val1<val2:
                    sum+=val2-val1
                    i+=2
                    continue
            sum+=val1
            i+=1
        return sum
        