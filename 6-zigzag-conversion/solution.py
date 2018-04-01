
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        buffer = [[] for _ in range(numRows)]
        pivot, repeat = numRows - 2, max(2 * (numRows - 1), 1)
        for i, char in enumerate(s):
            if i % repeat <= pivot:
                buffer[i % repeat] += [char]
            else:
                buffer[pivot - (i % repeat)] += [char]
        return ''.join([''.join(row) for row in buffer])
