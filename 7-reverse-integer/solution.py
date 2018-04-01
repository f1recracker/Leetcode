
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign, rev = 1 if x > 0 else -1, 0
        x *= sign
        while x > 0:
            rev = 10 * rev + (x % 10)
            x //= 10
        if rev > 0x7FFFFFFF:
            rev = 0
        return rev * sign
