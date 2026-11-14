from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        INF = float('inf')
        best = INF

        for i in range(n):
            # end index j (exclusive) must satisfy l <= j - i <= r
            for j in range(i + l, min(i + r, n) + 1):
                s = prefix[j] - prefix[i]
                if 0 < s < best:
                    best = s

        return -1 if best == INF else best