from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq1=Counter(nums1)
        freq2=Counter(nums2)
        ls=[]
        st=set(nums1)
        for i in st:
                count=min(freq2[i],freq1[i])
                while count>0:
                    ls.append(i)
                    count-=1
        return ls
        