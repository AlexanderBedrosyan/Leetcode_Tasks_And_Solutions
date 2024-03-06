# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the
# original letters exactly once.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        information = {}

        for ch in strs:
            sorted_ch = ''.join(sorted(ch))
            if sorted_ch not in information:
                information[sorted_ch] = []
            information[sorted_ch].append(ch)

        return [current_list for current_list in information.values()]


solve = Solution()
print(solve.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))