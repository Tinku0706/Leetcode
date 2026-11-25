class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        if start<0 or start>=len(arr):
            return False
        if arr[start]==0:
            return True
        if arr[start]==-1:
            return False
        jump=arr[start]
        arr[start]=-1

        return (self.canReach(arr,start+jump) or self.canReach(arr,start-jump))        