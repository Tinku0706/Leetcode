class Solution:
    def jump(self, nums: list[int]) -> int:
       currentindex=0
       jumps=0
       maxindex=0
       for i in range(len(nums)-1):
          maxindex=max(maxindex,i+nums[i])
          
          if i==currentindex:
            jumps+=1
            currentindex=maxindex
       return jumps

        