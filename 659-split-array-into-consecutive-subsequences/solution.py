
from heapq import heappush, heappop

class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        buffers = Heap(key=lambda x: (x[-1], len(x)))
        for num in nums:
            print(buffers.heap)
            buffer = buffers.extract_min()
            if buffer and buffer[-1] + 1 == num:
                buffer += [num]
            else: buffer = [num]
            buffers.heapify(buffer[:])
        for buffer in buffers.heap:
            if len(buffer) < 3:
                return False
        return True

class Heap:
    def __init__(self, key=None):
        self.elements = 0
        self.key = key or (lambda x: x)
        self.heap = []
    def extract_min(self):
        if len(self.heap) == 0: return None
        l_iter = lambda x: 2 * x + 1
        r_iter = lambda x: 2 * x + 2
        min_val, self.heap[0] = self.heap[0], self.heap[-1]
        self.heap = self.heap[:len(self.heap) - 1]
        h_iter = 0
        while True:
            l_key = self.key(self.heap[l_iter(h_iter)]) if l_iter(h_iter) < len(self.heap) else None
            r_key = self.key(self.heap[r_iter(h_iter)]) if r_iter(h_iter) < len(self.heap) else None
            if l_key is None and r_key is None: break
            if l_key < self.heap[h_iter] < r_key: break
            if r_key is None or l_key < r_key:
                self.heap[h_iter], self.heap[l_iter(h_iter)] = self.heap[l_iter(h_iter)], self.heap[h_iter]
                h_iter = l_iter(h_iter)
            else:
                self.heap[h_iter], self.heap[r_iter(h_iter)] = self.heap[r_iter(h_iter)], self.heap[h_iter]
                h_iter = r_iter(h_iter)
        return min_val
    def heapify(self, item):
        self.heap += [item]
        h_iter = len(self.heap) - 1
        while self.key(self.heap[h_iter]) < self.key(self.heap[h_iter // 2]):
            self.heap[h_iter], self.heap[h_iter // 2] = self.heap[h_iter // 2], self.heap[h_iter]
            h_iter //= 2
