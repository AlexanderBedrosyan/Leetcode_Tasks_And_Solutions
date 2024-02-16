# You are given an integer array nums sorted in non-decreasing order.
#
# Build and return an integer array result with the same length as nums such that result[i] is
# equal to the summation of absolute differences between nums[i] and all the other elements in the array.
#
# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sums = [0] * n
        suffix_sums = [0] * n

        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i - 1] + (i * (nums[i] - nums[i - 1]))

        for i in range(n - 2, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + ((n - 1 - i) * (nums[i + 1] - nums[i]))

        result = [0] * n
        for i in range(n):
            result[i] = prefix_sums[i] + suffix_sums[i]

        return result


solve = Solution()
print(solve.getSumAbsoluteDifferences([2,3,5]))