class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])

        count=0
        end_time=intervals[0][1]

        for i in range(1,len(intervals)):
            if intervals[i][0]>=end_time:
                end_time=intervals[i][1]
            else:
                count+=1
        return count


            
        