# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zig_zag_dict = {}

        for i in range(numRows):
            zig_zag_dict[i] = ''

        num = 0

        while num != len(s):

            for i in range(numRows):
                num += 1
                zig_zag_dict[i] += s[num - 1]
                if num == len(s):
                    break

            if numRows == 2:
                continue

            if num == len(s):
                break

            for i in range(numRows - 2, 0, -1):
                num += 1
                zig_zag_dict[i] += s[num - 1]
                if num == len(s):
                    break

        print(''.join(zig_zag_dict.values()))



solve = Solution()
solve.convert("PAYPALISHIRING", 3)
solve.convert("PAYPALISHIRING", 4)
solve.convert('A', 1)