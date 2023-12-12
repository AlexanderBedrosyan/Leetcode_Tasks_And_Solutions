# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# First Solution

# class Solution:
#     def isValid(self, s: str) -> bool:
#         starting_parentheses = '{(['
#         valid_parentheses = ['{}', '()', '[]']
#         new_string = ''
#         for letter in s:
#             if letter in starting_parentheses:
#                 new_string += letter
#                 continue
#             if letter not in starting_parentheses and not new_string:
#                 new_string += letter
#                 break
#             if new_string[-1] + letter in valid_parentheses:
#                 new_string = new_string[:-1]
#             else:
#                 break
#
#         return False if new_string else True

# Second Solution:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_parentheses = {'}': '{', ')': '(', ']': '['}

        for char in s:
            if char in valid_parentheses:
                if not stack or stack.pop() != valid_parentheses[char]:
                    return False
            else:
                stack.append(char)

        return not stack