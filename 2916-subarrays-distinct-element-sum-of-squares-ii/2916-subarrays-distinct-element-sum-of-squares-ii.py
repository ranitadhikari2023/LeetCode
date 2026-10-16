class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        s = [0] * (2 * size)    # sum of f
        sq = [0] * (2 * size)   # sum of f^2
        lz = [0] * (2 * size)   # lazy add
        ln = [0] * (2 * size)   # segment length
        for i in range(size, 2 * size):
            ln[i] = 1
        for i in range(size - 1, 0, -1):
            ln[i] = ln[2 * i] * 2

        def apply(o, v):
            sq[o] = (sq[o] + 2 * v * s[o] + v * v * ln[o]) % MOD
            s[o] = (s[o] + v * ln[o]) % MOD
            lz[o] += v

        def push(o):
            if lz[o]:
                apply(2 * o, lz[o])
                apply(2 * o + 1, lz[o])
                lz[o] = 0

        def update(o, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(o, 1)
                return
            push(o)
            m = (l + r) // 2
            if ql <= m:
                update(2 * o, l, m, ql, qr)
            if qr > m:
                update(2 * o + 1, m + 1, r, ql, qr)
            s[o] = (s[2 * o] + s[2 * o + 1]) % MOD
            sq[o] = (sq[2 * o] + sq[2 * o + 1]) % MOD

        last = {}
        ans = 0
        for j, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, size - 1, p + 1, j)
            ans = (ans + sq[1]) % MOD
            last[x] = j
        return ans