# You are given two strings a and b of the same length. Choose an index and split both strings at the
# same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and
# splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or
# bprefix + asuffix forms a palindrome.
#
# When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty.
# For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.
#
# Return true if it is possible to form a palindrome string, otherwise return false.
#
# Notice that x + y denotes the concatenation of strings x and y.

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(s, i, j):
            return s[i:j + 1] == s[i:j + 1][::-1]

        def check(a, b):
            i, j = 0, len(a) - 1
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            return is_palindrome(a, i, j) or is_palindrome(b, i, j)

        return check(a, b) or check(b, a)

solve = Solution()
print(solve.checkPalindromeFormation("aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd", "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"))