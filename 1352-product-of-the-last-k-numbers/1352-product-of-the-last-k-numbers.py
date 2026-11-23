class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]  # sentinel; prefix[i] = product of the first i nonzero numbers since last zero

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # a zero wipes out every earlier product
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):  # window includes a zero
            return 0
        return self.prefix[-1] // self.prefix[-k - 1]