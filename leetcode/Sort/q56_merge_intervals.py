class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key= lambda x: x[0])
        output = [intervals[0]]
        idx = 1

        while idx < len(intervals):
            if intervals[idx][0] <= output[-1][1]:
                output[-1] = [output[-1][0], max(output[-1][1], intervals[idx][1])]
            else:
                output.append(intervals[idx])
            idx += 1

        return output



