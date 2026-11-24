from collections import Counter
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        mp1=Counter(nums)
        for key,value in mp1.items():
            if value>1:
                return True
        return False

        