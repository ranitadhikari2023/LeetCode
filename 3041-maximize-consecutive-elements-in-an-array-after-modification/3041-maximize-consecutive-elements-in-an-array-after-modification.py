from typing import List

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}          # dp[v] = longest run ending at value v
        ans = 1
        for x in nums:
            # Use x as x+1 first (reads old dp[x])
            a = dp.get(x, 0) + 1
            # Use x as x (reads dp[x-1], untouched by this element)
            b = dp.get(x - 1, 0) + 1
            if a > dp.get(x + 1, 0):
                dp[x + 1] = a
            if b > dp.get(x, 0):
                dp[x] = b
            ans = max(ans, a, b)
        return ans