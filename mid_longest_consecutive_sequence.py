# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.

from typing import List

# Solution 1:
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         final_result = 0
#         current_result = 1 if nums else 0
#         new_list = sorted(nums)
#         for i in range(len(nums)):
#             if i != len(nums) - 1 and new_list[i] + 1 == new_list[i + 1]:
#                     current_result += 1
#             elif i != len(nums) - 1 and new_list[i] == new_list[i + 1]:
#                 continue
#             else:
#                 if final_result < current_result:
#                     final_result = current_result
#                 current_result = 1
#         return final_result if final_result > current_result else current_result


# Solution 2
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak