# Given a string columnTitle that represents the column title as appears in an Excel sheet,
# return its corresponding column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        list_of_items = [ord(ch) - 64 for ch in columnTitle]
        total_sum = 0
        count_of_rows = 26 ** (len(list_of_items) - 1)

        if len(list_of_items) > 1:
            for ch in list_of_items[0:len(list_of_items) - 1]:
                total_sum += (ch * count_of_rows)
                count_of_rows /= 26

        total_sum += list_of_items[-1]
        return int(total_sum)


# A B C D E...