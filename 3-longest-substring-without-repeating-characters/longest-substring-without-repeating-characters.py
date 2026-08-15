class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index=res=0
        st=set()
        for i in s:
            while i in st:
                st.remove(s[index])
                index+=1
            st.add(i)
            res=max(res,len(st))
        return res
        