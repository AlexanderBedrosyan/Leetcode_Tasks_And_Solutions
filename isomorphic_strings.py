# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two
# characters may map to the same character, but a character may map to itself.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mapping_s_t = {} 
        mapping_t_s = {}
        for char_s, char_t in zip(s, t):
            if char_s in mapping_s_t:
                if mapping_s_t[char_s] != char_t:
                    return False
            else:
                mapping_s_t[char_s] = char_t


            if char_t in mapping_t_s:
                if mapping_t_s[char_t] != char_s:
                    return False
            else:
                mapping_t_s[char_t] = char_s

        return True


solution = Solution()
result = solution.isIsomorphic("egg", "add")
print(result)

solve = Solution()
print(solve.isIsomorphic('paper', 'title'))