class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=elemnt=0
        for i in nums:
            if count==0:
                elemt=i
            if i==elemt:
                count+=1
            else:
               count-=1
        return elemt
        