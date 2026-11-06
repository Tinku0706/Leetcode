class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        temp=[]

        def backtrack(ind):
            ans.append(temp.copy())
            for i in range(ind,len(nums)):
                temp.append(nums[i])
                backtrack(i+1)
                temp.pop()

        backtrack(0)
        return ans
            
            


        