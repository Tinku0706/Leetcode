class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start=0
        current_gas=0
        total_gas=0
        for i in range(len(gas)):
            diff=gas[i]-cost[i]
            current_gas+=diff
            total_gas+=diff

            if current_gas<0:
                current_gas=0
                start=i+1
        if total_gas<0:
            return -1
        return start

        