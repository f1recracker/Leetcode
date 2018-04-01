
from itertools import groupby

class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0: return False
        self.nums = nums
        self.k = k
        self.target = sum(nums) // k
        if max(nums) > self.target: return False
        return self.dfs([None for _ in nums])
    
    def dfs(self, assignments):
        for group, vals in groupby(zip(assignments, self.nums), key=lambda x: x[0]):
            if group is not None and sum(vals) > self.target:
                break
        if None in assignments:
            target_index = assignments.index(None)
            for group in range(self.k):
                new_assignments = assignments[:]
                new_assignments[target_index] = group
                if self.dfs(new_assignments):
                    return True
        else:
            return True
