class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp1=Counter(s)
        mp2=Counter(t)
        for key,value in mp1.items():
            if key not in mp2 or value!=mp2[key]:
                return False
        return True

        
        