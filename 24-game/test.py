
from solution import Solution

test_cases = [
    ([4, 1, 8, 7], True),
    ([1, 2, 1, 2], False),
    ([8, 1, 6, 6], True),
    ([1, 1, 7, 7], False),
    ([3, 3, 8, 8], True),
]

if __name__ == '__main__':
    sol = Solution()
    for i, test_case in enumerate(test_cases):
        x, y = test_case
        assert sol.judgePoint24(x) == y, 'Test case #%d failed' % (i + 1)
    print('All test cases passed')
