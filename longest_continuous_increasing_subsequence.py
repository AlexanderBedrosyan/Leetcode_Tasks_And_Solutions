# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence
# (i.e. subarray). The subsequence must be strictly increasing.
#
# A continuous increasing subsequence is defined by two indices l and r (l < r)
# such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length = 0
        current_length = 0

        def check_if_max_should_be_changed():
            nonlocal current_length, max_length
            if current_length > max_length:
                max_length = current_length
            current_length = 0

        for i in range(len(nums)):
            if i == 0:
                current_length += 1
                continue
            if nums[i] > nums[i - 1]:
                current_length += 1
            else:
                if current_length == 0:
                    current_length += 1
                else:
                    check_if_max_should_be_changed()
                    current_length += 1
        check_if_max_should_be_changed()
        return max_length


solve = Solution()
print(solve.findLengthOfLCIS([2,2,2,2,2]))