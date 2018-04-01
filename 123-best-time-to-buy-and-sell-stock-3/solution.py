
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Best and 2nd best past price (lower is better)
        past_best_1 = [(float('inf'), 0) for _ in prices]
        past_best_2 = [(float('inf'), 0) for _ in prices]
        # Best and 2nd best future price (higher is better)
        future_best_1 = [(float('-inf'), 0) for _ in prices]
        future_best_2 = [(float('-inf'), 0) for _ in prices]
        for i in range(1, len(prices)):
            past_best_1[i] = min(past_best_1[i - 1], (prices[i - 1], 1 - i))
            if past_best_1[i - 1] < (prices[i - 1], 1 - i):
                past_best_2[i] = min(past_best_2[i - 1], (prices[i - 1], 1 - i))
            else: past_best_2[i] = past_best_1[i - 1]
        for i in range(len(prices) - 1)[::-1]:
            future_best_1[i] = max(future_best_1[i + 1], (prices[i + 1], -i - 1))
            if future_best_1[i + 1] > (prices[i + 1], -i - 1):
                future_best_2[i] = max(future_best_2[i + 1], (prices[i + 1], -i - 1))
            else: future_best_2[i] = future_best_1[i + 1]

        print(prices)
        print(past_best_1)
        print(past_best_2)
        print(future_best_1)
        print(future_best_2)
        print()
