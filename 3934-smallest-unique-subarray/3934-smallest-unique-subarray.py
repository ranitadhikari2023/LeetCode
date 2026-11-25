from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        size = 2 * n + 2
        nxt = [None] * size          # transitions as dicts (values up to 1e5)
        link = [-1] * size
        length = [0] * size
        cnt = [0] * size

        nxt[0] = {}
        sz, last = 1, 0

        for c in nums:
            cur = sz; sz += 1
            length[cur] = length[last] + 1
            cnt[cur] = 1
            nxt[cur] = {}
            p = last
            while p != -1 and c not in nxt[p]:
                nxt[p][c] = cur
                p = link[p]
            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][c]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = sz; sz += 1
                    length[clone] = length[p] + 1
                    nxt[clone] = nxt[q].copy()
                    link[clone] = link[q]
                    cnt[clone] = 0
                    while p != -1 and nxt[p].get(c) == q:
                        nxt[p][c] = clone
                        p = link[p]
                    link[q] = link[cur] = clone
            last = cur

        # propagate occurrence counts along suffix links (longest first)
        order = sorted(range(1, sz), key=lambda v: -length[v])
        for v in order:
            cnt[link[v]] += cnt[v]

        ans = n
        for v in range(1, sz):
            if cnt[v] == 1:
                ans = min(ans, length[link[v]] + 1)
        return ans