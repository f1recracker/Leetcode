
class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        distances = sorted([(abs(x - item), item) for item in arr])
        return sorted([item for _, item in distances][:k])
