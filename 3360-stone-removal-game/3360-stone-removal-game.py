class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice_turn = True
        k = 10
        while k > 0 and n >= k:
            n -= k
            k -= 1
            alice_turn = not alice_turn
        # The player whose turn it is now cannot move and loses
        return not alice_turn