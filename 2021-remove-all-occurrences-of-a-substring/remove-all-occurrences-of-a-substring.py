class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            i = s.find(part)
            s = s[:i] + s[i + len(part):]   #Keep everything before part + keep everything after part → effectively delete part.
        return s
        
        