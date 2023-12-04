# Task Two Sums:
#
# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution - 1:

        # index = 0
        # while index < (len(nums) - 1):
        #     current_num = nums[index]
        #     for i in range(index + 1, len(nums)):
        #         if current_num + nums[i] == target:
        #             return [index, i]
        #     index += 1
        # return []

        # Solution - 2:
        # result = [[i, index] for i in range(len(nums)) for index in
        # range(i + 1, len(nums)) if nums[i] + nums[index] == target]
        # if result:
        #     return [result[0][0], result[0][1]]
        # return []

        # Solution - 3:
        # result = [[i, index] for i in range(len(nums)) for index in
        # range(i + 1, len(nums)) if nums[i] + nums[index] == target]
        # try:
        #     return [result[0][0], result[0][1]]
        # except IndexError:
        #     return []

        # Solution - 4:
        return [[i, index] for i in range(len(nums)) for index in range(i + 1, len(nums)) if nums[i] + nums[index] == target][0]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
