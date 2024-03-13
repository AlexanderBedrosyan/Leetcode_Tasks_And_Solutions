# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i.
# In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1].
# The test cases are generated such that you can reach nums[n - 1].

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        max_reachable = nums[0]
        last_jump = nums[0]
        jumps = 1

        for i in range(1, len(nums)):
            if i > last_jump:
                jumps += 1
                last_jump = max_reachable
            max_reachable = max(max_reachable, i + nums[i])

solve = Solution()
print(solve.jump([1]))
