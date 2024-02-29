# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which
# does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        checked_numbers = []

        while True:
            new_sum = sum(int(ch) * int(ch) for ch in str(n))

            if new_sum == 1:
                return True

            if new_sum in checked_numbers:
                return False

            checked_numbers.append(new_sum)
            n = new_sum

solve = Solution()
print(solve.isHappy(2))