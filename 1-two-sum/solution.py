
class Solution(object):
    def twoSum(self, nums, target):
        indices = {}
        for index, num in enumerate(nums):
            if target - num in indices and indices[target - num] != index:
                return [indices[target - num], index]
            indices[num] = index
