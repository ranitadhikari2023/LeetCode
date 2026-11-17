class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # proper divisors for each length
        divs = [[] for _ in range(n + 1)]
        for d in range(1, n + 1):
            for m in range(2 * d, n + 1, d):
                divs[m].append(d)   # d is a proper divisor of m

        # cost[i][j]: min changes to make s[i..j] a semi-palindrome
        cost = [[INF] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                best = INF
                for d in divs[length]:
                    m = length // d
                    c = 0
                    for g in range(d):
                        lo, hi = i + g, i + g + (m - 1) * d
                        while lo < hi:
                            if s[lo] != s[hi]:
                                c += 1
                            lo += d
                            hi -= d
                    best = min(best, c)
                    if best == 0:
                        break
                cost[i][j] = best

        # dp[p][j]: min cost splitting s[:j] into p parts
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] < INF and cost[i][j - 1] < INF:
                        v = dp[p - 1][i] + cost[i][j - 1]
                        if v < dp[p][j]:
                            dp[p][j] = v
        return dp[k][n]