# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
# the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
# "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if not s:
            return True

        splitted_s = [ch for ch in s]

        for ch in t:

            if not splitted_s:
                break

            current_letter = splitted_s.pop(0)

            if current_letter == ch:
                continue

            splitted_s.insert(0, current_letter)

        return True if not splitted_s else False


solve = Solution()
print(solve.isSubsequence('aec', 'abcde'))
