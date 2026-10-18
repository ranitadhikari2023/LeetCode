MOD = 10**9 + 7

class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        n = len(nums)
        # Pascal triangle for C(i, j) mod MOD
        C = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i-1][j-1] + C[i-1][j]) % MOD

        def dfs(arr: list[int]) -> int:
            m = len(arr)
            if m < 3:
                return 1
            root = arr[0]
            left  = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]
            ways = C[m-1][len(left)]
            ways = ways * dfs(left)  % MOD
            ways = ways * dfs(right) % MOD
            return ways

        return (dfs(nums) - 1) % MOD