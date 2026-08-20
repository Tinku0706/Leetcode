class Solution:
    def beautySum(self, s: str) -> int:
        sum=0
        for i in range(len(s)):
            mp=Counter()
            for j in range(i,len(s)):
                mp[s[j]]+=1
                if len(mp)>=2:
                    sum+=(max(mp.values())-min(mp.values()))
        return sum

        