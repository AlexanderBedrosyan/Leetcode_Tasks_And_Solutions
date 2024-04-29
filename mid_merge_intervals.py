# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
# of the non-overlapping intervals that cover all the intervals in the input.

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
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
print(solve.merge([[1,3],[2,6],[8,10],[15,18]]))
print(solve.merge([[1, 4], [4, 5]]))
print(solve.merge([[1, 4], [0, 4]]))
print(solve.merge([[1, 4], [0, 1]]))
print(solve.merge([[1, 4], [0, 0]]))
print(solve.merge([[1, 4], [0, 2], [3, 5]]))
print(solve.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))