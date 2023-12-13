# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.

from typing import List

# Solution 1
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         number_as_string = ''.join(str(ch) for ch in digits)
#         as_one_more = str(int(number_as_string) + 1)
#         return [int(ch) for ch in as_one_more]


# Solution 2
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 != 10:
            digits[-1] += 1
            return digits
        number_as_string = ''.join(str(ch) for ch in digits)
        as_one_more = str(int(number_as_string) + 1)
        return [int(ch) for ch in as_one_more]


solve = Solution()
print(solve.plusOne([1,2,3]))