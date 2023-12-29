# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        for ch in unique_nums:
            if nums.count(ch) > len(nums) // 2:
                return ch


solve = Solution()
print(solve.majorityElement([2,2,1,1,1,2,2]))
