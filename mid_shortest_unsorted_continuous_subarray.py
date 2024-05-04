# Given an integer array nums, you need to find one continuous subarray such that
# if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
#
# Return the shortest such subarray and output its length.

# from typing import List

# Solution 1:
# class Solution:
#     def findUnsortedSubarray(self, nums: List[int]) -> int:
#         new_list = []
#         starting_list = [ch for ch in nums]
#         while nums:
#             min_chart = min(nums)
#             new_list.append(min_chart)
#             nums.remove(min_chart)
#
#         diff_area = [i for i, ch in enumerate(new_list) if ch != starting_list[i]]
#         return len([1 for _ in range(diff_area[0], diff_area[-1] + 1)]) if diff_area else 0

from typing import List

# Solution 2:
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        start, end = 0, n - 1

        while start < n - 1 and nums[start] <= nums[start + 1]:
            start += 1

        if start == n - 1:
            return 0

        while end > 0 and nums[end] >= nums[end - 1]:
            end -= 1

        min_val = min(nums[start:end + 1])
        max_val = max(nums[start:end + 1])

        while start > 0 and nums[start - 1] > min_val:
            start -= 1

        while end < n - 1 and nums[end + 1] < max_val:
            end += 1

        return end - start + 1


solve = Solution()
print(solve.findUnsortedSubarray([2,6,4,8,10,9,15]))