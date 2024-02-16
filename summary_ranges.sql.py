# You are given a sorted unique integer array nums.
#
# A range [a,b] is the set of all integers from a to b (inclusive).
#
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
# That is, each element of nums is covered by exactly one of the ranges,
# and there is no integer x such that x is in one of the ranges but not in nums.
#
# Each range [a,b] in the list should be output as:
#
# "a->b" if a != b
# "a" if a == b
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        new_list = []
        starting_index = []

        def full_the_new_list():
            if len(starting_index) > 1:
                new_list.append(f"{starting_index[0]}->{starting_index[-1]}")
            else:
                new_list.append(f"{starting_index[0]}")

        for i, ch in enumerate(nums):
            if starting_index and starting_index[-1] != ch - 1:
                full_the_new_list()
                starting_index = [ch]
            else:
                starting_index.append(ch)

            if i == len(nums) - 1:
                full_the_new_list()
        return new_list


solve = Solution()
print(solve.summaryRanges([0,2,3,4,6,8,9]))