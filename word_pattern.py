# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        pattern = [ch for ch in pattern]
        s = s.split(' ')
        if len(pattern) != len(s):
            return False

        info = {}

        for i in range(len(pattern)):
            if pattern[i] not in info:
                if info:
                    if s[i] in info.values():
                        return False
                info[pattern[i]] = s[i]
                continue

            if info[pattern[i]] != s[i]:
                return False

        return True




solve = Solution()
print(solve.wordPattern( "absa", "dog cat cat dog"))