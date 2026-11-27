class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        n = len(items)

        # g[i] = number of j != i with factor_i | factor_j
        g = [0] * n
        for i in range(n):
            fi = items[i][0]
            cnt = 0
            for j in range(n):
                if j != i and items[j][0] % fi == 0:
                    cnt += 1
            g[i] = cnt

        # 0/1 knapsack: first copy of each item type
        dp = [0] * (budget + 1)  # dp[c] = best value with total cost <= c
        for i in range(n):
            price = items[i][1]
            val = 1 + g[i]
            for c in range(budget, price - 1, -1):
                cand = dp[c - price] + val
                if cand > dp[c]:
                    dp[c] = cand

        # Leftover money buys the cheapest item repeatedly
        min_price = min(p for _, p in items)
        ans = 0
        for c in range(budget + 1):
            ans = max(ans, dp[c] + (budget - c) // min_price)
        return ans