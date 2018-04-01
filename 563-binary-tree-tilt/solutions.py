
class Solution:
    def findTilt(self, root, return_sum=False):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return (0, 0) if return_sum else 0
        left_tilt, left_sum = self.findTilt(root.left, True)
        right_tilt, right_sum = self.findTilt(root.right, True)
        val = root.val if root.val else 0
        tilt, sum_ = abs(left_sum - right_sum) + left_tilt + right_tilt, left_sum + right_sum + val
        return (tilt, sum_) if return_sum else tilt
