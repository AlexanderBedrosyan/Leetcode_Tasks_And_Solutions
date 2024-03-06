# You are given an integer array height of length n. There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_water = float('-inf')
        left, right = 0, len(height) - 1

        while left < right:
            vertical_column = min(height[left], height[right])
            distance = abs(left - right)

            max_water = max(max_water, distance * vertical_column)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_water

solve = Solution()
print(solve.maxArea([1,8,6,2,5,4,8,3,7]))
