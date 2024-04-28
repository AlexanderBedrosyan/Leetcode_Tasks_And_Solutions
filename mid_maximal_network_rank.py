# There is an infrastructure of n cities with some number of roads connecting these cities.
# Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.
#
# The network rank of two different cities is defined as the total number of directly connected roads to either city.
# If a road is directly connected to both cities, it is only counted once.
#
# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.
#
# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 0

        max_dict = {}

        for i in range(n):
            max_dict[i] = 0

        for array in roads:
            max_dict[array[0]] += 1
            max_dict[array[1]] += 1

        max_result = 0

        for i in range(n):
            for next_number in range(i + 1, n):
                current_score = max_dict[i] + max_dict[next_number]

                if [i, next_number] in roads or [next_number, i] in roads:
                    current_score -= 1

                max_result = max(max_result, current_score)

        return max_result

solve = Solution()
print(solve.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))