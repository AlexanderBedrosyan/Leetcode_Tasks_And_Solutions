# Given an array of integers citations where citations[i] is the number of citations a researcher received
# for their ith paper, return the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that
# the given researcher has published at least h papers that have each been cited at least h times.


class Solution(object):
    def hIndex(self, citations):

        sorted_citations = sorted(citations, reverse=True)
        last_result = 0
        for i in range(len(sorted_citations)):
            if sorted_citations[i] >= (i + 1):
                last_result = i + 1
            else:
                break
        return last_result

solve = Solution()
print(solve.hIndex([1]))