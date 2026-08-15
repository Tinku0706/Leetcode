class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        res=1
        res*=nums[len(nums)-1]-1
        res*=nums[len(nums)-2]-1
        return res
        