from itertools import permutations
from math import ceil

class Solution:
    def judgePoint24(self, nums):
        for nums in set(permutations(nums)):
            for ops_mask in range(4 * 4 * 4):
                if self.test([float(x) for x in nums], ops_mask):
                    return True
        return False

    def test(self, nums, ops_mask):
        ops, eval_orders = Solution.ops(ops_mask), permutations(range(3))
        for eval_order in eval_orders:
            if Solution.eval(nums[:], ops, eval_order):
                return True
        return False

    @staticmethod
    def eval(nums, ops, order):
        roots = UnionFind(len(nums))
        for _, (i, op) in sorted(zip(order, enumerate(ops))):
            p, q = roots.find(i), roots.find(i + 1)
            if nums[q] == 0 and op == '__truediv__':
                return False
            parent = roots.union(p, q)
            nums[parent] = getattr(nums[p], op)(nums[q])
        # print(nums_copy, ops, order, nums[roots.find(0)])
        return nums[roots.find(0)] == 24.0

    @staticmethod
    def ops(mask):
        decoder = {0: '__add__', 1: '__sub__', 2: '__mul__', 3: '__truediv__'}
        return [
            decoder[mask % 4], decoder[mask // 4 % 4], decoder[mask // 16 % 4]
        ]


class UnionFind:
    def __init__(self, size):
        self.root = {i: i for i in range(size)}

    def union(self, i, j):
        self.root[self.find(i)] = self.find(j)
        return self.find(j)

    def find(self, i):
        while self.root[i] != self.root[self.root[i]]:
            self.root[i] = self.root[self.root[i]]
        return self.root[i]
