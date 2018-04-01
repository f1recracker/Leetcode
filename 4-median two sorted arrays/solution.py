from bisect import bisect_left

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.mergedLength = len(nums1) + len(nums2)
        if self.mergedLength % 2:
            return self.getNthInMerged(self.mergedLength / 2)
        else:
            return (self.getNthInMerged(self.mergedLength / 2) + self.getNthInMerged(self.mergedLength / 2 - 1)) / 2
    
    def getNthInMerged(self, index, reverse=False):
        # Case 1: Neither fits
        if index > len(self.nums1) and index > len(self.nums2):
            return self.getNthInMerged(self.mergedLength - index, reverse=True)
        if not reverse:
            # Case 2: At least one fits
            larger, smaller = (self.nums1, self.nums2) if len(self.nums1) > self.nums2 else (self.nums2, self.nums1)
            index2 = bisect_left(smaller, larger[index])
        return None