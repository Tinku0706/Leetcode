class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq={}
        left=ans=0
        for right in range(len(nums)):
            freq[nums[right]]=freq.get(nums[right],0)+1 

            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans 

#freq = {1: 2, 2: 1, 3: 1}-then when i add 4th elemnt(1)
#freq becomes 1:2 means 2>2 while condiiton so i will remove leftmost elmt
# Because when left moves forward, we're removing that element from the sliding window.  