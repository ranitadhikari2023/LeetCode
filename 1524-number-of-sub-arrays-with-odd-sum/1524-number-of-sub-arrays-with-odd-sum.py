class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even, odd = 1, 0   # counts of prefix sums seen so far, by parity
        parity = 0         # parity of current prefix sum
        ans = 0

        for x in arr:
            parity ^= (x & 1)
            if parity:             # current prefix odd -> pair with earlier even prefixes
                ans += even
                odd += 1
            else:                  # current prefix even -> pair with earlier odd prefixes
                ans += odd
                even += 1

        return ans % MOD