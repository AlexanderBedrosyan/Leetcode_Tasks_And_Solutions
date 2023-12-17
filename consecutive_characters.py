# The power of the string is the maximum length of a non-empty substring that contains only one unique character.
#
# Given a string s, return the power of s.

class Solution:
    def maxPower(self, s: str) -> int:
        max_result = 0
        current_result = 0
        current_letter = ''
        for letter in s:
            if current_letter == '':
                current_letter = letter
                current_result += 1
                continue
            if letter == current_letter:
                current_result += 1
            else:
                if max_result < current_result:
                    max_result = current_result
                current_letter = letter
                current_result = 1
        if current_result > max_result:
            max_result = current_result
        return max_result
