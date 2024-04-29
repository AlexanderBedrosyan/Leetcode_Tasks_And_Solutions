# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float('inf')
        left_pointer = 0
        current_sum = 0

        for right_pointer in range(len(nums)):
            current_sum += nums[right_pointer]

            while current_sum >= target:
                min_length = min(min_length, right_pointer - left_pointer + 1)
                current_sum -= nums[left_pointer]
                left_pointer += 1

        return min_length if min_length != float('inf') else 0



solve = Solution()
print(solve.minSubArrayLen(7, [2,3,1,2,4,3]))
print(solve.minSubArrayLen(4, [1,4,4]))
# print(solve.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))