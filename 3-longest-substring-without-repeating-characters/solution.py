
from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length, last_index = 0, defaultdict(lambda: -1)
        substr_start = [-1] * len(s)
        for index, char in enumerate(s):
            substr_start[index] = max(substr_start[index - 1], last_index[char])
            max_length = max(max_length, index - substr_start[index])
            last_index[char] = index
        return max_length
