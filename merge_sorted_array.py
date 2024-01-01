# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and
# two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = m - 1
        ptr2 = n - 1
        total_ptr = m + n - 1

        # Merge nums1 and nums2 from the end
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[total_ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[total_ptr] = nums2[ptr2]
                ptr2 -= 1
            total_ptr -= 1

        # Add remaining elements from nums2 if any
        while ptr2 >= 0:
            nums1[total_ptr] = nums2[ptr2]
            ptr2 -= 1
            total_ptr -= 1
