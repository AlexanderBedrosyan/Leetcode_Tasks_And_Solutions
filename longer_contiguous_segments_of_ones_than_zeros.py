# Given a binary string s, return true if the longest contiguous segment of 1's is strictly
# longer than the longest contiguous segment of 0's in s, or return false otherwise.
#
# For example, in s = "110100010" the longest continuous segment of 1s has length 2, and
# the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's
# is considered to have a length 0. The same applies if there is no 1's.

import re

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zero_list = sorted(re.findall('[0]+',s), reverse=True)
        one_list = sorted(re.findall('[1]+', s), reverse=True)
        if zero_list and one_list:
            return len(zero_list[0]) < len(one_list[0])
        elif not zero_list and one_list:
            return True
        else:
            return False

solve = Solution()
print(solve.checkZeroOnes("110100010"))