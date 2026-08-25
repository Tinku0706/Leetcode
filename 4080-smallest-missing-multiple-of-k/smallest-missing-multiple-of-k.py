class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        maxv=max(nums)+k
        ans=0
        for i in range(k,maxv+1,k):
            if i not in nums:
                ans=i
                break
        return ans
        