# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented
# as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches
# between xstart and xend. You do not know the exact y-coordinates of the balloons.
#
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A
# balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number
# of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
#
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[1])
        total_number = 1
        strike = points[0][1]
        for element in points:

            if element[0] > strike:
                total_number += 1
                strike = element[1]

        return total_number

solve = Solution()
print(solve.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(solve.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(solve.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
print(solve.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
print(solve.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))