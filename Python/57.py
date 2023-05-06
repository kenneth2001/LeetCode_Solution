class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            else:
                newInterval = (min(interval[0], newInterval[0]), max(interval[1], newInterval[1]))
        
        return left + [newInterval] + right
    