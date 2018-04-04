
class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        suf_sum = [None for _ in nums] + [0]
        for i in range(len(nums))[::-1]:
            suf_sum[i] = suf_sum[i + 1] + nums[i]
        running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            if running_sum == suf_sum[i]:
                return i
        return -1