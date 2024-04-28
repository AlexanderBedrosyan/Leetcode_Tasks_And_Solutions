# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        longest_substring = ''
        max_charts = 0

        for i in range(n):
            longest_substring += s[i]
            current_charts = 1
            for j in range(i + 1, n):
                if s[j] not in longest_substring:
                    longest_substring += s[j]
                    current_charts += 1
                else:
                    longest_substring = ''
                    break
            max_charts = max(max_charts, current_charts)

        return max_charts

solve = Solution()
print(solve.lengthOfLongestSubstring("abcabcbb"))
print(solve.lengthOfLongestSubstring("bbbbb"))
print(solve.lengthOfLongestSubstring("pwwkew"))
print(solve.lengthOfLongestSubstring(" "))
