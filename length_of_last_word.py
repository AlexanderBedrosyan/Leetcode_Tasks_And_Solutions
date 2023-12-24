# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.


# Solution 1
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.strip().split(' ')[-1])


# Solution 2
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         result = ''
#         for item in s.strip()[::-1]:
#             if item == ' ':
#                 return len(result)
#             result += item
#         return len(result)

# Solution 3
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         result = ''
#         end = len(s) - 1
#         lend = 0
#         while end >= 0 and s[end] == ' ':
#             end -= 1
#
#         while end >= 0 and s[end] != ' ':
#             lend += 1
#             end -= 1
#
#         return lend

# Solution 4:
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split()[-1])


# class Solution 5 with 99 % win Memory consumption.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = ''
        s = s.strip()
        if ' ' not in s:
            return len(s)
        while True:
            if s[-(len(result) + 1)] == ' ':
                break
            result += s[-(len(result) + 1)]

        return len(result)

solve = Solution()
print(solve.lengthOfLastWord("  luffy is still joyboy  "))