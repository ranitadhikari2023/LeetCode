import random

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        k = len(nums) // 2

        def quickselect(arr, k):
            lo, hi = 0, len(arr) - 1
            while True:
                if lo == hi:
                    return arr[lo]
                pivot = arr[random.randint(lo, hi)]

                # 3-way partition (Dutch national flag): <pivot | ==pivot | >pivot
                lt, i, gt = lo, lo, hi
                while i <= gt:
                    if arr[i] < pivot:
                        arr[lt], arr[i] = arr[i], arr[lt]
                        lt += 1
                        i += 1
                    elif arr[i] > pivot:
                        arr[i], arr[gt] = arr[gt], arr[i]
                        gt -= 1
                    else:
                        i += 1

                if k < lt:
                    hi = lt - 1
                elif k > gt:
                    lo = gt + 1
                else:
                    return pivot

        median = quickselect(nums, k)
        return sum(abs(x - median) for x in nums)