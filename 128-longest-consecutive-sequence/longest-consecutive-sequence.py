class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        maxc=0
        s=set()
        for i in nums:
            s.add(i)
        for i in s:
            if i-1 not in s:
                count=1
                current=i
                while current+1 in s:
                    count+=1
                    current+=1
                maxc=max(maxc,count)
        return maxc
        