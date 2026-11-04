from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        m = len(vals)

        cnt = [0] * (m + 1)   # BIT of counts
        sm = [0] * (m + 1)    # BIT of sums

        def update(i, c, v):
            while i <= m:
                cnt[i] += c
                sm[i] += v
                i += i & -i

        def prefix(i):
            c = s = 0
            while i > 0:
                c += cnt[i]
                s += sm[i]
                i -= i & -i
            return c, s

        LOG = 1 << (m.bit_length() - 1)
        mid = (x + 1) // 2  # 1-indexed median position

        def kth():
            pos, rem, step = 0, mid, LOG
            while step:
                nxt = pos + step
                if nxt <= m and cnt[nxt] < rem:
                    pos = nxt
                    rem -= cnt[nxt]
                step >>= 1
            return pos + 1  # rank of the median value

        cost = [0] * (n - x + 1)
        total = 0
        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            total += nums[i]
            if i >= x:
                update(rank[nums[i - x]], -1, -nums[i - x])
                total -= nums[i - x]
            if i >= x - 1:
                r = kth()
                med = vals[r - 1]
                cL, sL = prefix(r)
                cost[i - x + 1] = (med * cL - sL) + ((total - sL) - med * (x - cL))

        INF = float('inf')
        prev = [0] * (n + 1)              # dp[0][*]
        for j in range(1, k + 1):
            cur = [INF] * (n + 1)
            for i in range(j * x, n + 1):
                cur[i] = min(cur[i - 1], prev[i - x] + cost[i - x])
            prev = cur
        return prev[n]