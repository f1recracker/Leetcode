
class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''
        left = ('(%s)' % self.tree2str(t.left)) if t.left else '()' if t.right else ''
        right = ('(%s)' % self.tree2str(t.right)) if t.right else ''
        current = str(t.val) if t.val is not None else ''
        return '%s%s%s' % (current, left, right)