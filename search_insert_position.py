# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

from typing import List


# Solution 1
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         return [i for i, value in enumerate(nums) if value >= target][0] if max(nums) >= target else len(nums)

# Solution 2
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         return nums.index([ch for ch in nums if ch >= target][0]) if max(nums) >= target else len(nums)

# Solution 3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, value in enumerate(nums):
          if value == target:
            return i
          elif value > target:
            return i
        return len(nums)

