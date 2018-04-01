
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        char_iter = iter(range(1, n))
        for i in char_iter:
            if chars[i] is None: continue
            rep_count = 0
            while i + rep_count < n and chars[i - 1] == chars[i + rep_count]:
                chars[i + rep_count] = None
                rep_count += 1
            if rep_count > 0:
                for j, num in enumerate(str(rep_count + 1)):
                    chars[i + j] = num
        # Flatten all none values
        j, none_vals = 0, 0
        for i in range(n):
            while j < n and chars[i] is None and chars[j] is None:
                none_vals += 1
                j += 1
            if j == n: break
            chars[i], chars[j] = chars[j], chars[i]
            j += 1
        return n - none_vals
