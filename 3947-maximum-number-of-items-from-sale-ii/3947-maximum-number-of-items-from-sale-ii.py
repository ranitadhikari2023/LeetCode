from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cnt = [0] * (n + 1)
        for f, _ in items:
            cnt[f] += 1

        # M[f] = number of items whose factor is a multiple of f
        M = [0] * (n + 1)
        for f in range(1, n + 1):
            M[f] = sum(cnt[f::f])          # harmonic-sum total: O(n log n)

        c = min(p for _, p in items)       # cheapest price -> used for single copies

        # (price, number of double-value copies available)
        doubles = []
        for f, p in items:
            d = M[f] - 1
            if d > 0 and p <= 2 * c:
                doubles.append((p, d))
        doubles.sort()

        total = 0
        rem = budget
        for p, d in doubles:
            t = min(d, rem // p)
            if t == 0:
                break                      # later prices are >= p, also unaffordable
            total += 2 * t
            rem -= t * p

        return total + rem // c