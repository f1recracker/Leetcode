
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return s
        n = len(s)
        opt = [[0 for _j in range(len(s) + 1)] for _i in range(len(s) + 1)]
        for pal_len in range(n + 1):
            for i in range(n - pal_len):
                j = i + pal_len
                if j == i:
                    opt[i][j] = 1
                elif opt[i + 1][j - 1] == j - i - 1 and s[i] == s[j]:
                    opt[i][j] = j - i + 1
                else:
                    opt[i][j] = max(opt[i + 1][j - 1], opt[i + 1][j], opt[i][j - 1])
        return self.backtrace(opt, s)
    
    def backtrace(self, opt, s):
        i, j = 0, len(s) - 1
        target = opt[i][j]
        while j - i + 1 > target:
            _, i, j = max((opt[i + 1][j], i + 1, j),
                          (opt[i][j - 1], i, j - 1),
                          (opt[i + 1][j - 1], i + 1, j - 1))
        return s[i:j + 1]
