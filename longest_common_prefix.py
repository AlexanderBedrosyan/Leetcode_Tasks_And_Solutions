# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_list = sorted(strs, key=lambda element: len(element))
        started_element = sorted_list[0]
        needed_element = ''
        for element in started_element:
            result = all(True if (needed_element + element) in current_element[:len(needed_element + element)] else False for current_element in sorted_list[1:])
            if not result:
                break
            needed_element += element
        return needed_element


solve = Solution()
print(solve.longestCommonPrefix(["flower","flow","flight"]))
print(solve.longestCommonPrefix(["dog","racecar","car"]))