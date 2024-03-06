# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the
# start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an
# interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals
# still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])

        if len(intervals) == 1:
            return sorted(intervals)

        counter = 0

        while counter < len(intervals) - 1:
            first = intervals[counter]
            second = intervals[counter + 1]
            sorted_list = sorted(first + second)

            if first == [sorted_list[0], sorted_list[1]] and sorted_list[1] != sorted_list[2]:
                counter += 1
                continue

            if second == [sorted_list[0], sorted_list[1]] and sorted_list[1] != sorted_list[2]:
                intervals[counter], intervals[counter + 1] = intervals[counter + 1], intervals[counter]
                counter += 1
                continue

            intervals[counter][0], intervals[counter][1] = sorted_list[0], sorted_list[3]
            intervals.remove(second)


        return intervals

solve = Solution()
print(solve.insert([[1,3],[6,9]], [2, 5]))