# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Solution 1
# from typing import List
#
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         for _ in range(k):
#             ch = nums.pop()
#             nums.insert(0, ch)

# Solution 2 - this one gave me 100% beats for Runtime
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])