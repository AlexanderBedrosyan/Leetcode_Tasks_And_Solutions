# Given an integer array nums sorted in non-decreasing order, remove some duplicates
# in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Custom Judge:
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index_list = []
        used_items = {}

        for i in range(len(nums)):
            if nums[i] not in used_items:
                used_items[nums[i]] = 0
            if used_items[nums[i]] == 2:
                index_list.append(i)
                continue
            else:
                used_items[nums[i]] += 1

        for element in index_list[::-1]:
            nums.pop(element)

        return len(nums)


solve = Solution()
print(solve.removeDuplicates([1,1,1,2,2,3]))
