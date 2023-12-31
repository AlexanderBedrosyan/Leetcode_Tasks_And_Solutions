# Given a binary array nums, return the maximum number of consecutive 1's in the array.
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        current_length = 0
        def is_current_length_higher_than_max_length():
            nonlocal max_length, current_length
            if max_length < current_length:
                max_length = current_length
        for element in nums:
            if element == 1:
                current_length += 1
            else:
                is_current_length_higher_than_max_length()
                current_length = 0
        is_current_length_higher_than_max_length()
        return max_length

solve = Solution()
print(solve.findMaxConsecutiveOnes([1,1,0,1,1,1]))